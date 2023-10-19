from tkinter import *
from googletrans import Translator

window = Tk()
window.title("English - Turkish translation")
window.minsize(400,400)
window.maxsize(400,400)
window.config(background="black")

translator = Translator()

def Translationn():
    input_text = entry_one.get()
   
    if input_text == "":
        label_three.config(text="Please don't leave it empty")
    else:
        translation = translator.translate(input_text,src='en', dest='tr')
        label_three.config(text=f"{translation.text}")

label_one = Label(text="English", background="yellow")
label_one.config(height=5, width=18)
label_one.pack(pady=10)

entry_one = Entry()
entry_one.pack(pady=10)

button_one = Button(text="Translate", command=Translationn)
button_one.config(width=15, height=3)
button_one.pack(pady=10)

label_two = Label(text="Turkish", background="red")
label_two.config(height=5, width=18)
label_two.pack(pady=10)

label_three = Label()
label_three.pack(pady=5)

window.mainloop()