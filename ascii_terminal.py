from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import html, sys

IMAGE = Path(sys.argv[1] if len(sys.argv) > 1 else "profile.webp")
COLS = 42
RAMP = " .:-=+*#%@"

img = Image.open(IMAGE).convert("L")
img = ImageOps.autocontrast(img)
img = ImageEnhance.Contrast(img).enhance(1.25)
w, h = img.size
img = img.crop((int(w*0.08), int(h*0.02), int(w*0.92), int(h*0.82)))
new_h = max(1, int(img.height / img.width * COLS * 0.48))
img = img.resize((COLS, new_h))

rows = []
for y in range(new_h):
    line = ""
    for x in range(COLS):
        p = img.getpixel((x, y))
        idx = int((255-p)/255*(len(RAMP)-1))
        line += RAMP[idx]
    rows.append(line.rstrip())

print("\n".join(rows))
