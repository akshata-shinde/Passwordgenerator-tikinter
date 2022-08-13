from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("600x600")
root.title("Python Password Generator")

def GeneratePassword():
    
    ReturnPass_Entry.delete(0, END)
    Get_PassLength = int(PassLength_Entry.get())

    
    LowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
    UppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Numbers = "1234567890"
    Symbols = "!@#$%^&*()<>?"
    
    for i in range(0, Get_PassLength):
        Password = random.choice(LowercaseLetters + UppercaseLetters + Numbers + Symbols)
        ReturnPass_Entry.insert(END, Password)


def CopyToClipboard():
    root.clipboard_append(ReturnPassword_Entry.get())
    messagebox.showinfo(title="Password Was Copied to Clipboard", message="Your Password Was Successfully Copied to Your Clipboard")

Title = Label(root, text="Python Password Generator", font=("Arial", 30))
Title.pack()

MainFrame = Frame(root)
MainFrame.pack(pady=60)

PasswordLength_Label = Label(MainFrame, text="Password Length:", font=("Arial", 20))
PasswordLength_Label.pack()

PassLength_Entry = Entry(MainFrame, font=("Arial", 16))
PassLength_Entry.pack()
              
ReturnPassword_Entry = Entry(MainFrame, font=("Arial", 26), bg="dodgerblue")
ReturnPassword_Entry.pack(pady=36)

GenPassBtn = Button(MainFrame, text="Generate Password", width=16, height=1, font=("Arial", 14), command=GeneratePassword)
GenPassBtn.pack()
    
CopyToClipboardBtn = Button(MainFrame, text="Copy to Clipboard", width=16, height=1, font=("Arial", 14), command=CopyToClipboard) 
CopyToClipboardBtn.pack()

root.mainloop()

         



