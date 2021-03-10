import os
from tkinter import *
from tkinter import ttk
from gtts import gTTS
import tkinter.font as font
from playsound import playsound
from googletrans import Translator


root = Tk()
root.geometry('500x500')
root.title('Traduction')
root.configure(background='#CACACA')
root.iconbitmap(r'image/icon.ico')
root.resizable(0,0)
my_font = font.Font(family='Helvetica', size=13, weight='bold')

style = ttk.Style()
style.configure('TLabel',background='#CACACA')
h1 = ttk.Label(root,text="DETECT AUTOMATIC LANGUAGE",font=('Helvetica', 12, 'bold'))
h1.pack(pady=16)
frame_1 = Frame(root)
frame_1.pack(pady=5)
frame_1.configure(background='#CACACA')

scroll_y = Scrollbar(frame_1)
scroll_y.grid(row=1,column=3,sticky='NSW',pady=10)
text_tran = Text(frame_1,width=50,height=10,yscrollcommand=scroll_y.set)
text_tran.grid(row=1,column=1,columnspan=2,pady=10)

btn1 = Button(frame_1,text='Translation')
btn1 ['font'] = my_font
btn1.grid(row=2,column=0,columnspan=2)

choices = ["EN","FR","AR","ES"]
lang_choice = ttk.Combobox(frame_1,value=choices,width=7)
lang_choice.grid(row=2,column=1,columnspan=2)
lang_choice.current(0)

btn2 = Button(frame_1,text='Clear')
btn2 ['font'] = my_font
btn2.grid(row=2,column=2,columnspan=2)

frame_2 = Frame(root)
frame_2.pack(pady=5)
frame_2.configure(background='#CACACA')

volum_img = PhotoImage(file='image/volume.png')

scroll_y2 = Scrollbar(frame_2)
scroll_y2.grid(row=1,column=3,sticky='NSW',pady=10)
text_to = Text(frame_2,width=50,height=10,yscrollcommand=scroll_y2.set)
text_to.grid(row=1,column=1,columnspan=2,pady=10)
img_btn = Button(frame_2,image=volum_img,borderwidth=0)
img_btn.grid(row=1,column=4,pady=10,padx=2)
img_btn.configure(background='#CACACA')

scroll_y.config(command=text_tran.yview)
scroll_y2.config(command=text_to.yview)
def tradure():
    global afichage
    global langue
    langue = lang_choice.get()
    langue = langue.lower()
    x = text_tran.get(1.0,END)
    trons = Translator()
    try:
        os.system('del hello.mp3')
    except:
        pass
    afichage = trons.translate(x, dest=langue)
    text_to.delete(1.0,END)
    text_to.insert(INSERT,afichage.text)
    

def clear():
    text_tran.delete(1.0,END)
    text_to.delete(1.0,END)

def volume():
    tts = gTTS(afichage.text, lang=langue)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    os.system('del hello.mp3')


btn1.config(command=tradure)
btn2.config(command=clear)
img_btn.config(command=volume)
root.mainloop()