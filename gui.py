import tkinter as tk


# # Function to update the balance
def update_balance():
    try:
        amount = float(balance_entry.get())
        current_balance = float(label.cget("text").split("$")[1])
        new_balance = current_balance + amount
        label.config(text=f"Balance: ${new_balance:.2f}")
        balance_entry.delete(0, tk.END)
    except ValueError:
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, "Invalid Input")


# Create the main window
root = tk.Tk()
root.title("Finance Planner")
root.geometry("1280x720")

# Create two frames
left_frame = tk.Frame(root)
right_frame = tk.Frame(root, bg="lightgreen")

# Place the frames in a grid
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")

# Configure the grid to make each frame take up half 
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)  # The font of the front half shortens the back half
root.grid_rowconfigure(0, weight=1)

# Add widgets to the left frame
label = tk.Label(left_frame, text="Balance: $0", font=("Arial", 35))
label.pack(pady=50)

# Create an entry to input the amount
balance_entry = tk.Entry(left_frame)
balance_entry.pack()

# Create a button to update the balance
update_button = tk.Button(left_frame, text="Add to Balance", command=update_balance)
update_button.pack(pady=5)

root.mainloop()
