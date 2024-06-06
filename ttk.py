import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("ttk Widgets Example")

# Create and place a label
label = ttk.Label(root, text="This is a Label")
label.pack(padx=10, pady=5)

# Create and place a button
button = ttk.Button(root, text="This is a Button")
button.pack(padx=10, pady=5)

# Create and place a checkbutton
checkbutton = ttk.Checkbutton(root, text="This is a Checkbutton")
checkbutton.pack(padx=10, pady=5)

# Create and place a combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.set("Select an Option")
combobox.pack(padx=10, pady=5)

# Create and place an entry
entry = ttk.Entry(root)
entry.pack(padx=10, pady=5)

# Create and place a progressbar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(padx=10, pady=5)
progress["value"] = 100

# Run the main loop
root.mainloop()
