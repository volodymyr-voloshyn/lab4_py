from translator_pkg.mod_deep import *

text = "Добрий день"

print(TransLate(text,"auto","fr"))

print(LangDetect(text))

LanguageList("screen", text)