from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = GoogleTranslator(source=scr, target=dest).translate(text) # Створення об'єкта перекладача з вказанням мови-джерела та цільової мови
        return result
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set="all"):

    try:
        lang = detect(text)
        if set == "lang":
            return lang
        elif set == "confidence":
            return "Unknown"
        else:
            return lang # Повернення коду мови за замовчуванням
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str):
    return lang

def LanguageList(out="screen", text=None):
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    rows = []
    for name, code in langs.items():
        translation = ""

        if text:
            try:
                translation = GoogleTranslator(source='auto', target=code).translate(text) # Виконання перекладу фрази на кожну ітерацію циклу для нової мови
            except:
                translation = "error"
        rows.append((code, name, translation))

    if out == "screen":
        print(f"{'CODE':<10}{'LANGUAGE':<20}{'TRANSLATION':<30}")
        for r in rows:
            print(f"{r[0]:<10}{r[1]:<20}{r[2]:<30}")
    return "Ok"