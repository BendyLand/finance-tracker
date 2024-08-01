import tkinter as tk
import re


def update_balance_text(entry, label):
    val = entry.get()
    val = re.search("[0-9]+", val)
    current = label.cget("text")
    current = re.search("[0-9]+", current)
    total = "0"
    if current is not None and val is not None:
        total = str(int(val[0]) + int(current[0]))
        result = "Balance: $" + total
        label.config(text=result)
    entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Finance Planner")
root.geometry("1280x720")

nw_frame = tk.Frame(bg="lightgreen")
sw_frame = tk.Frame(bg="lightblue")
r_frame = tk.Frame(bg="pink")

nw_frame.grid(row=0, column=0, sticky="nsew")
sw_frame.grid(row=1, column=0, sticky="nsew")
r_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")

root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

label = tk.Label(nw_frame, text="Balance: $0", font=("Arial", 50), bg="lightgreen")
label.pack(pady=50)

entry = tk.Entry(nw_frame)
entry.pack()

button = tk.Button(
    nw_frame, text="Add", command=lambda: update_balance_text(entry, label)
)
button.pack(pady=25)

tk.Label(sw_frame, text="Can I Afford?", font=("Arial", 50), bg="lightblue").pack(
    pady=10
)

tk.Label(r_frame, text="Bills:", font=("Arial", 50), bg="pink").pack(pady=25)


root.mainloop()
