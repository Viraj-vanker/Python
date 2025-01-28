import tkinter as tk
root=tk.Tk()
root.title("layout with pack")
root.geometry("300x200")

tk.Label(root,text="Top",bg="lightblue").pack(side="top",fill="x")
tk.Label(root,text="Bottom",bg="lightgreen").pack(side="bottom",fill="x")
tk.Label(root,text="Left",bg="lightcoral").pack(side="left",fill="y")
tk.Label(root,text="Right",bg="lightyellow").pack(side="right",fill="y")

root.mainloop()