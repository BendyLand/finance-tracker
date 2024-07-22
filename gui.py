import tkinter as tk

root = tk.Tk()

root.title("Finance Tracker")

label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()

root.mainloop()
