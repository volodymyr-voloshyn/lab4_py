import json
import os  
import re #регуляр. вирази для складного пошуку та обробки тексту

from translator_pkg.mod_gtrans4 import TransLate, LangDetect

with open("config.json") as f:
    config = json.load(f) # Перетворення вмісту JSON-файлу у зручний словник Python
filename = config["file"]
if not os.path.exists(filename):
    print("File not found")
    exit()
with open(filename, encoding="utf8") as f:
    text = f.read()

size = os.path.getsize(filename)
chars = len(text)
words = len(text.split())
sentences = len(re.findall(r'[.!?]', text))
lang = LangDetect(text, "lang")

print("File:", filename)
print("Size:", size, "bytes")
print("Characters:", chars)
print("Words:", words)
print("Sentences:", sentences)
print("Language:", lang)

translated = TransLate(text, "auto", config["dest"])
if config["output"] == "screen":
    print("\nTranslated text:\n")
    print(translated)
elif config["output"] == "file":
    newfile = filename + "_" + config["dest"] + ".txt"
    with open(newfile, "w", encoding="utf8") as f:
        f.write(translated)
    print("Ok")