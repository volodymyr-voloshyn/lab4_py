from translator_pkg.mod_gtrans4 import *

text = "Добрий день"

print(TransLate(text, "auto", "fr"))

print(LangDetect(text))

print(CodeLang("french"))

LanguageList("screen", text)