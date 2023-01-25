import os
import sys
import time

from gtts import gTTS
from pypdf import PdfReader

from dcpy import clear

language = "en"


def main():

    if len(sys.argv) == 1:
        clear()
        text = input("Input the text you want me to say!\n\n")
        translate_text = gTTS(text=text, lang=language)
        translate_text.save("output.mp3")
        os.system("mpv output.mp3")

    elif len(sys.argv) == 2:
        # Get pages
        path = sys.argv[1]
        reader = PdfReader(path)
        pages = reader.pages

        filename = os.path.splitext(path)[0]

        with open(f"{filename}.mp3", "wb") as file:

            for i, page in enumerate(pages):
                clear()

                print("Extracting page data...")
                data = " ".join(page.extract_text().split())

                translate_page = gTTS(text=data, lang=language)

                print(f"Converting page text to mp3 | {i + 1}/{len(pages)}")

                try:
                    translate_page.write_to_fp(file)
                except:
                    print("You are rate limited rip man...")
                    continue
                time.sleep(5)
    else:
        print("Please specify a pdf to convert!")
        return 1


main()
