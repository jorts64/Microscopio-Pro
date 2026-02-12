import tkinter as tk
from tkinter import simpledialog, messagebox


def ask_string(title, prompt):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    value = simpledialog.askstring(title, prompt, parent=root)
    root.destroy()
    return value


def show_error(title, message):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror(title, message, parent=root)
    root.destroy()
