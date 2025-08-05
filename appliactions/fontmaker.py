import sys
from PIL import Image
import os
import inkscape

# --- Configuration --- # Replace with your image name
filename = '/New Piskel.png'
IMG_PATH = os.path.dirname(sys.argv[0]) + filename
OUTPUT_DIR = "glyphs"
GLYPH_WIDTH = 8
GLYPH_HEIGHT = 8
COLUMNS = 16  # in the image
ROWS = 8
START_CODE = 0  # ASCII 0

def safe_char(c):
    # Replace non-printable or invalid filename characters
    if c in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
        return 'char' + str(ord(c))
    elif ord(c) < 32 or ord(c) == 127:
        return 'nonprint'
    else:
        return c

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load image
img = Image.open(IMG_PATH).convert("1")  # 1-bit image (black & white)

i = 0
for row in range(ROWS):
    for col in range(COLUMNS):
        left = col * GLYPH_WIDTH  # Left boundary of the current glyph
        upper = row * GLYPH_HEIGHT  # Upper boundary of the current glyph
        right = left + GLYPH_WIDTH  # Right boundary of the current glyph
        lower = upper + GLYPH_HEIGHT  # Lower boundary of the current glyph

        # Crop the glyph from the image
        glyph_img = img.crop((left, upper, right, lower))

        # Assign ASCII code to each character (starting from 0)
        ascii_code = START_CODE + i

        # If the ASCII code is printable (between 32 and 126), use its character, else label it as 'nonprint'
        char = chr(ascii_code)
        safe_name = safe_char(char)
        glyph_img.save(f"{OUTPUT_DIR}/{ascii_code:03}_{safe_name}.png")

        i += 1

print("✅ Glyphs extracted and saved.")
