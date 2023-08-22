from tkinter import *
import os
import time


def on_entry_click(event):
    if text.get() == "Enter Text Here":
        text.delete(0, END)
        text.config(fg="black")
    
def texttospeech():
    
    tx = txt.get()
    if tx != "":
        txt1.set("Speaking...")
        statusbar.update()
        #time.sleep(1)
        command = f'echo "{tx}" | powershell -command "& {{Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())}}"'
        os.system(command)
        
    text.delete(0,END)
    txt1.set("Created By Irtaza Manzoor")
    statusbar.update()
    


root = Tk()
root.geometry("500x400")
root.minsize(500,400)
root.title("  Robo Speaker")
root.wm_iconbitmap("robo2.ico")
root.configure(bg="black")
Label(root, text="Robo Speaker", fg="White", bg="grey", font="lucida 30 bold").pack(side=TOP, fill=X)
txt = StringVar()
txt.set("")
text = Entry(root, textvariable=txt, font="lucida 20", fg="grey", borderwidth=6)
text.insert(0, "Enter Text Here")
text.bind("<FocusIn>", on_entry_click)
text.pack(pady=20)

btn = Button(root, text="Speak!!", padx=20, pady=5, borderwidth=6, bg="Light blue", font="lucida 10 bold", command=texttospeech)
btn.pack(pady=10)

txt1 = StringVar()
txt1.set("Created By Irtaza Manzoor")
statusbar = Label(root, textvariable = txt1, bg="white", fg="black", pady=10, font="lucida 10 bold")
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
     