import tkinter as tk
def v():
    label.config(text="button pressed")
root = tk.Tk()
root.title("label change")
root.geometry("400x200")

button=tk.Button(root,text="button",command=v)
button.pack(pady=20)

label = tk.Label(root,text="button not pressed")
label.pack(pady=20)

root.mainloop()