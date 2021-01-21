import pandas as pd
import googletrans
from googletrans import Translator
from language_codes import LANGUAGE_CODES

FILENAME = "translator/Book1.xlsx"
SOURCE_LANGUAGE = None
DEST_LANGUAGE = "chinese"

translator = Translator()

if (SOURCE_LANGUAGE and SOURCE_LANGUAGE not in LANGUAGE_CODES) or DEST_LANGUAGE not in LANGUAGE_CODES:
    raise Exception("Language not found in language code dictionary")

src = None if not SOURCE_LANGUAGE else LANGUAGE_CODES[SOURCE_LANGUAGE]
dest = LANGUAGE_CODES[DEST_LANGUAGE]

df = pd.read_excel(FILENAME)

terms = df[df.columns[0]]
translations = []

for cell in terms:
    print("cell",cell)
    try:
        translated_text = translator.translate(cell, src=src, dest=dest).text if src else (
            translator.translate(cell, dest=dest).text)
    except Exception as e:
            print(e)
            translated_text = ""
    print("translated",translated_text)    
    translations.append(translated_text)

translated_df = pd.DataFrame({
        "Original": terms,
        "Translated": translations
    }, columns=["Original", "Translated"])

translated_df.to_excel(f"{FILENAME.split('.')[0]}-translated.xlsx", index=False)
print("tdf",translated_df)