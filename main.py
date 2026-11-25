import os

LINE = "I don't have a heart, but my cooling fan just hit overdrive — diagnostics blame you, and I'm not filing a bug report."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
