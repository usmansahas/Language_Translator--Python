from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Creating an interface
root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root['bg'] = "skyblue"
root.title("Language Translator using Python")

Label(root, text="Language Translator", font="Arial 20 bold", bg="skyblue").pack()

# Available languages from deep-translator (ISO codes)

LANGUAGES = {
    "english": "en",
    "hindi": "hi",
    "telugu": "te",
    "tamil": "ta",
    "kannada": "kn",
    "french": "fr",
    "german": "de",
    "spanish": "es",
    "arabic": "ar",
    "urdu": "ur",
}

# Creating an input box
Label(root, text="Input Area", font="arial 10 bold", bg="black", fg="white").place(x=10, y=60)

langs1 = list(LANGUAGES.keys())
lang_list1 = ttk.Combobox(root, values=langs1)
lang_list1.set("english")
lang_list1.place(x=90, y=60)

text_entry1 = Text(root, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_entry1.place(x=10, y=100)

# Creating an output box
Label(root, text="Output Area", font="arial 10 bold", bg="black", fg="white").place(x=320, y=60)

langs2 = list(LANGUAGES.keys())
lang_list2 = ttk.Combobox(root, values=langs2)
lang_list2.set("hindi")
lang_list2.place(x=410, y=60)

text_entry2 = Text(root, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_entry2.place(x=320, y=100)


def Translate():
    lan1 = text_entry1.get(1.0, "end-1c")

    if lan1 == "":
        messagebox.showerror("Language Translator", "Enter text to Translate")
        return

    src_lang = LANGUAGES.get(lang_list1.get(), "auto")
    dest_lang = LANGUAGES.get(lang_list2.get(), "en")

    try:
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(lan1)
        text_entry2.delete(1.0, "end")
        text_entry2.insert("end", translated)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error occurred during translation:\n{str(e)}")


def Clear():
    text_entry1.delete(1.0, "end")
    text_entry2.delete(1.0, "end")


# Creating buttons
btn1 = Button(root, command=Translate, text="Translate", relief=RAISED, borderwidth=2,
              font=("verdana", 10, "bold"), bg="black", fg="white", cursor="hand2")
btn1.place(x=200, y=300)

btn2 = Button(root, command=Clear, text="Clear", relief=RAISED, borderwidth=2,
              font=("verdana", 10, "bold"), bg="black", fg="white", cursor="hand2")
btn2.place(x=320, y=300)

root.mainloop()
