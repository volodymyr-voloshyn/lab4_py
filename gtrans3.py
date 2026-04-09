from translator_pkg.mod_gtrans3 import TransLate, LangDetect, CodeLang, LanguageList

text = "Good day"

# Переклад
translated = TransLate(text, "auto", "fr")
print(translated)

# Визначення мови
lang = LangDetect(text, "all")
print(lang)

# Код мови
code = CodeLang("uk")
print(code)

# Таблиця мов
LanguageList("screen", text)