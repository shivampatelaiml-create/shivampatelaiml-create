from pathlib import Path
import html, subprocess, sys

# Simple helper that regenerates the ASCII preview from profile.webp.
# The ready-to-use dark_mode.svg and light_mode.svg are already included.
img = sys.argv[1] if len(sys.argv) > 1 else "profile.webp"
subprocess.run([sys.executable, "ascii_terminal.py", img], check=True)
print("ASCII preview generated in terminal.")
print("Use the included dark_mode.svg and light_mode.svg in your README.")
