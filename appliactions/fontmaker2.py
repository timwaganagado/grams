import fontforge
import os

font = fontforge.font()
font.fontname = "PixelFont8x8"
font.familyname = "PixelFont8x8"
font.fullname = "PixelFont8x8"
font.encoding = "UnicodeFull"

GLYPH_DIR = "glyphs"
EM_SIZE = 1024  # High resolution for clean scaling
SCALE = EM_SIZE // 8  # Scale up 8x8 to fit EM square

for file in sorted(os.listdir(GLYPH_DIR)):
    if file.endswith(".png"):
        ascii_code = int(file.split("_")[0])
        char = chr(ascii_code)

        glyph = font.createChar(ascii_code, char)
        glyph.importOutlines(os.path.join(GLYPH_DIR, file), ("loadMode", "bitmap"))
        glyph.transform((SCALE, 0, 0, SCALE, 0, 0))
        glyph.width = EM_SIZE

font.generate("PixelFont8x8.ttf")
print("✅ Font generated.")