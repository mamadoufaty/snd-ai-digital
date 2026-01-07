from pypdf import PdfReader
import json

# Read LinkedIn PDF
try:
    reader = PdfReader("./data/snd.pdf")
    snd = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            snd += text
except FileNotFoundError:
    snd = "La SND est non disponible"

# Read other data files
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)