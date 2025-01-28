import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path=filedialog.askopenfilename(title="open a file")
    if file_path:
        label.config(text=f"select a file: {file_path}")
root = tk.Tk()
root.title("file open dialog")
root.geometry("400x200")

button = tk.Button(root,text="open file",command=open_file)
button.pack(pady=20)
label=tk.Label(root,text="no file selected")
label.pack(pady=20)

root.mainloop()