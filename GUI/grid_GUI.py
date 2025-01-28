import tkinter as tk

root = tk.Tk()
root.title("Layout with grid")
root.geometry("300x200")

tk.Label(root,text="0,0",bg="lightblue").grid(row=0,column=0,padx=5,pady=5)
tk.Label(root,text="0,1",bg="lightgreen").grid(row=0,column=1,padx=5,pady=5)
tk.Label(root,text="1,0",bg="lightcoral").grid(row=1,column=0,padx=5,pady=5)
tk.Label(root,text="1,1",bg="lightyellow").grid(row=1,column=1,padx=5,pady=5)

root.mainloop()