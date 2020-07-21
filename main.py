from tkinter import *
from tkinter.ttk import *
import webbrowser
import ctypes
import os
import winsound
import pyttsx3

root = Tk()

root.title("Text to Speech software by Devendra")

root.geometry("500x400+432+144")
root.resizable(0,0)

lbl1 = Label(text="This is a Text to speech software written in python")
lbl1.place(x="20", y="15")


# Main function
def speakbtn():
    if(input.get() == ''):
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        ctypes.windll.user32.MessageBoxW(16, "Please enter a value", "Error!", 16)
        # return False

    else:
        engine = pyttsx3.init()
        engine.say(input.get())
        dir = os.getcwd()
        engine.save_to_file(input.get(), f'{dir}/speech-to-text.mp3')
        saveinfo = Label(root, text=f"File saved in {dir}")
        saveinfo.place(x=20, y=200)
        # print(f"file saved to {dir}")
        engine.runAndWait()



url = "https://www.github.com/devendrapoonia"
new = 1


def openweb():
    webbrowser.open(url, new=new)


button1 = Button(root, text="Follow me on Github", command=openweb)
button1.place(x="350", y="15")

input = Entry(root, width=75)
input.place(x="23", y="100")


lbl2 = Label(root, text="Enter Text:")
lbl2.place(x=20, y=70)

speakbtn = Button(root, text="Speak", command=speakbtn)
speakbtn.place(x=140, y=150)

exit = Button(root, text="Exit", command=root.destroy)
exit.place(x=270, y=150)

root.mainloop()
