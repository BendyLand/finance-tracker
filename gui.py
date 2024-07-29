import tkinter as tk

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

tk.Label(nw_frame, text="Balance: $0", font=("Arial", 50), bg="lightgreen").pack(
    pady=10
)

tk.Label(sw_frame, text="Can I Afford?", font=("Arial", 50), bg="lightblue").pack(
    pady=10
)

tk.Label(r_frame, text="Bills:", font=("Arial", 50), bg="pink").pack(pady=25)


root.mainloop()
