import os
import pdfplumber
from sentence_transformers import SentenceTransformer
import numpy as np
import requests

# 1. Extract text from all PDFs in a folder
def extract_texts_from_pdfs(pdf_folder):
    all_chunks = []
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            # Chunk each paper
            chunks = chunk_text(text)
            all_chunks.extend(chunks)
    return all_chunks

# 2. Chunk text (same as before)
def chunk_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# 3. Embed all chunks
pdf_folder = "/Users/burto/RAG academic"  # Change to your folder
chunks = extract_texts_from_pdfs(pdf_folder)
print(f"Total chunks from all papers: {len(chunks)}")

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)

# 4. Retrieval and Ollama as before
def search(query, chunks, embeddings, model, top_k=3):
    query_emb = model.encode([query])[0]
    scores = np.dot(embeddings, query_emb)
    top_indices = np.argsort(scores)[-top_k:][::-1]
    return [chunks[i] for i in top_indices]

def ask_ollama(context, question, model="llama3"):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    try:
        data = response.json()
        return data.get("response", data)
    except Exception as e:
        print("Error parsing Ollama response:", e)
        print("Raw response text:", response.text)
        return None

# 5. Example query
query = "Summarize what makes a strong paper."
results = search(query, chunks, embeddings, model)
context = "\n".join(results)
answer = ask_ollama(context, query)
print("\nLLM Answer:\n", answer)

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Example: Use your own PDF as the prompt
user_pdf = "/Users/burto/Downloads/test essay.pdf"  # Path to your PDF
user_text = extract_text_from_pdf(user_pdf)

query = "Give detailed feedback and suggestions for improvement for the following essay."
results = search(query, chunks, embeddings, model)
context = "\n".join(results)

# Combine context and your PDF text
full_context = f"{context}\n\nEssay:\n{user_text}"

answer = ask_ollama(full_context, query)
print("\nLLM Feedback:\n", answer)