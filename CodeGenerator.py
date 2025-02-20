import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_steam_code():
    valid_chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    
    def random_block():
        return ''.join(random.choices(valid_chars, k=5))
    
    return f"{random_block()}-{random_block()}-{random_block()}"

def generate_and_display():
    code = generate_steam_code()
    code_var.set(code)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(code_var.get())
    root.update()

root = tk.Tk()
root.title("Code generator")
root.geometry("400x200")

code_var = tk.StringVar()

label = tk.Label(root, text="Code:")
label.pack(pady=10)

entry = tk.Entry(root, textvariable=code_var, font=("Monaco", 15), justify='center', state='readonly')
entry.pack(pady=5)

button_generate = tk.Button(root, text="click for a code", command=generate_and_display)
button_generate.pack(pady=5)

button_copy = tk.Button(root, text="Copy", command=copy_to_clipboard)
button_copy.pack(pady=5)

root.mainloop()
