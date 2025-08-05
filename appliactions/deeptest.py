from ollama import chat
from ollama import ChatResponse

import re
allmesages = []
def ask_deepseek(input_content, system_prompt, deep_think = True, print_log = True):
    allmesages.append({'role' : 'system', 'content' : system_prompt})
    allmesages.append({'role' : 'user', 'content' : input_content})
    response: ChatResponse = chat(model='deepseek-r1', messages=allmesages)
    response_text = response['message']['content']
    if print_log: print(response_text)
    # Extract everything inside <think>...</think> - this is the Deep Think
    think_texts = re.findall(r'<think>(.*?)</think>', response_text, flags=re.DOTALL)
    # Join extracted sections (optional, if multiple <think> sections exist)
    think_texts = "\n\n".join(think_texts).strip()
    # Exclude the Deep Think, and return the response
    clean_response= re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL).strip()

    # Return either the context, or a tuple with the context and deep think
    return clean_response if not deep_think else (clean_response, think_texts)

ask_deepseek("how large are tennis balls","you are a AI assistant")
ask_deepseek("what was my last prompt","you are a AI assistant")