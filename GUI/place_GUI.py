import tkinter as tk

root = tk.Tk()
root.title("Layout with place")
root.geometry("300x200")

tk.Label(root,text="Top left",bg="lightblue").place(x=10,y=20)
tk.Label(root,text="bottom right",bg="lightcoral").place(x=200,y=150)
tk.Label(root,text="Center",bg="lightgreen").place(relx=0.5,rely=0.5,anchor="center")

root.mainloop()