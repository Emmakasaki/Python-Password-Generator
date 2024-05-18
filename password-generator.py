
import random
import customtkinter as ctk
import tkinter as tk
import sys
import os
from tkinter import filedialog

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '_', '~']



charCount = 0
passCount = 0


def genPass():
    
    try:
        num = int(numEntry.get())
        char = int(charEntry.get())
        password = []
        for nums in range(num):
            for chars in range(char):
                password.append(random.choice(characters))
            passList.insert(tk.END, ''.join(password))
            password.clear()
    except:
        pass
    

def passSave():
    docPath = os.path.expanduser('~/Documents')
    passwords = passList.get(0, tk.END)
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=os.path.expanduser('~/Documents'), initialfile="passwordSave", title="Save Passwords", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if filePath:
        with open(filePath, 'w') as f:
            for password in passwords:
                f.write(password + '\n')

def clearPassList():
    passList.delete(0, tk.END)

root = ctk.CTk()
root.title("Password Generator")
root.geometry("1280x720")

numLabel = ctk.CTkLabel(root, text="Number of passwords:")
numEntry = ctk.CTkEntry(root)
charLabel = ctk.CTkLabel(root, text="Password length:")
charEntry = ctk.CTkEntry(root)
genButton = ctk.CTkButton(root, text="Generate Passwords", command=genPass, fg_color="red", corner_radius=30, hover_color="dark red")
clearButton = ctk.CTkButton(root, text="Clear Passwords", command=clearPassList, fg_color="red", corner_radius=30, hover_color="dark red")
passFrame = ctk.CTkFrame(root)
passScrollbar = ctk.CTkScrollbar(passFrame)
passList = tk.Listbox(passFrame, width=40, height=20, yscrollcommand=passScrollbar.set)
passScrollbar.configure(command=passList.yview)
saveButton = ctk.CTkButton(root, text="Save to file", fg_color="red", corner_radius=30, hover_color="dark red", command=passSave)

numLabel.pack()
numEntry.pack()
charLabel.pack()
charEntry.pack()
genButton.pack(), clearButton.pack()
passScrollbar.pack(side=ctk.RIGHT, fill=tk.Y)
passList.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
passFrame.pack()
saveButton.pack()


root.mainloop()