
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("350x300")
root.title("Keylogger Project")

def butaction():
    print("Keylogger Started")

empty = tk.Label(root,text="Keylogger Project",font ='Vardana 11 bold').grid(row=2,column=2)

Button(root,text='Start Keylogger',command= butaction).grid(row=5,column=2)


root.mainloop()