from googletrans import Translator, LANGUAGES
translator = Translator() 
def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text) # Визначення мови тексту та рівня впевненості

        if set == "lang":
            return detection.lang 
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"{detection.lang} ({detection.confidence})"

    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    try:
        for code, name in LANGUAGES.items():
            if lang.lower() == name.lower(): # Якщо введено назву мови повертаємо код
                return code
            if lang.lower() == code:
                return name
        return "Language not found"
    except:
        return "Error"

def LanguageList(out="screen", text=None):
    try:
        rows = []
        for code, name in LANGUAGES.items():
            translation = ""
            if text:
                try:
                    translation = translator.translate(text, dest=code).text # Переклад вказаного тексту на кожну мову зі списку Google Translate
                except:
                    translation = "error"
            rows.append((code, name, translation))
        if out == "screen":
            print(f"{'CODE':<10}{'LANGUAGE':<20}{'TRANSLATION':<30}") # Форматований вивід заголовка з вирівнюванням стовпців по лівому краю
            for r in rows:
                print(f"{r[0]:<10}{r[1]:<20}{r[2]:<30}") # Вивід рядка даних з аналогічним вирівнюванням
        elif out == "file":
            with open("languages.txt", "w", encoding="utf8") as f:
                f.write(f"{'CODE':<10}{'LANGUAGE':<20}{'TRANSLATION':<30}\n")
                for r in rows:
                    f.write(f"{r[0]:<10}{r[1]:<20}{r[2]:<30}\n")
        return "Ok"
    except Exception as e:
        return f"Error: {e}"