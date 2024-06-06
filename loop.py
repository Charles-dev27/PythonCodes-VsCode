import tkinter as tk 
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry('670x500')
window.configure(bg='khaki')

first_name = ['Charles', 'Jhon', 'Lara', 'Jessa']
last_name = ['Racho', 'Doe', 'Bautista', 'Sombillia']

treeview = ttk.Treeview(window, columns=('first', 'second', 'email'), show='headings')
treeview.heading('first', text='First')
treeview.heading('second', text='Second')
treeview.heading('email', text='email')
treeview.pack(fill='both', expand=True)

for i in range(100):
    first = choice(first_name)
    second =  choice(last_name)
    email = f'{first}{second}@gmail.com'
    data = (first, second, email)
    treeview.insert(parent='', index=0, values=data)

window.mainloop()