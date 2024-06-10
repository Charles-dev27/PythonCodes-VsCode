import tkinter as tk
from tkinter import messagebox, ttk

window = tk.Tk()
window.title('Login')
window.config(bg='Khaki')
window.geometry('550x440')

# Check if the user entry has all this characters
def is_valid_user(user):
    if (len(user) >= 8 and
        any(c.isalpha() for c in user) and
        any(c.isdigit() for c in user)):
        return True
    return False

# Check if the password entry has all this characters
def is_valid_password(password):
    if (len(password) >= 8 and
        (any(c.isalpha() for c in password)or '@'in password) and
        any(c.isdigit() for c in password) and
        any(c in '!@#$%^&*()-_=+{}[]";:.,></' for c in password)):
        return True
    return False

#update the user indicator label if all requirements are met
def on_user_change(*args):
    user = user_valid.get()
    if is_valid_user(user):
        user_indicator.config(text='✔Valid Username', fg='green')
    else:
        user_indicator.config(text='❌Invalid Username', fg='red')

#update the password indicator label if all requirements are met
def on_pass_change(*args):
    password = password_valid.get()
    if is_valid_password(password):
        password_indicator.config(text='✔Valid Password', fg='green')
    else:
        password_indicator.config(text='❌Invalid Password', fg='red')

#show and hide logic
def show_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_pass_btn.config(text='Show')
    else:
        password_entry.config(show='')
        show_pass_btn.config(text='Hide')

#Check if all reuiremets are met otherwise it will show an error
def login():
    user = username_entry.get()
    password = password_entry.get()
    masked_password = '*' * len(password)
    if is_valid_user(user) and is_valid_password(password):
        messagebox.showinfo('Login Success', f'Welcome {user} 👋🏾')
        tree.insert('', 'end', values=(user, masked_password))
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror('Login Unsuccsesful', 'Please Try Again')

#deletes a value inside the treeview
def delete():
    selected = tree.selection()
    if selected:
        tree.delete(selected)
    else:
        messagebox.showwarning('Invalid', 'Please Select Atleast One(1) Items Below')

main_frame = tk.LabelFrame(window, text='Login Form', font=('arial', 15), fg='purple', bg='khaki', padx=20, pady=20)
main_frame.pack(expand=True, fill='both', padx=20, pady=20, anchor='center')

login_label = tk.Label(main_frame, text='Username', fg='brown', bg='khaki', font=('arial', 10, 'bold'))
user_valid = tk.StringVar()
user_valid.trace('w', on_user_change) 
login_label.pack()

username_entry = tk.Entry(main_frame, textvariable=user_valid)
username_entry.pack()

user_indicator = tk.Label(main_frame, text='', bg='khaki')
user_indicator.pack()

password_label = tk.Label(main_frame, text='Password', fg='brown', bg='khaki', font=('arial', 10, 'bold'))
password_valid = tk.StringVar()
password_valid.trace('w', on_pass_change)
password_label.pack()

password_entry = tk.Entry(main_frame, textvariable=password_valid, show='*')
password_entry.pack()

password_indicator = tk.Label(main_frame, text='', bg='khaki')
password_indicator.pack()

show_pass_btn = tk.Button(main_frame, text='Show', bg='khaki', fg='brown', font=('arial', 10, 'bold'), command=show_password)
show_pass_btn.place(x=300, y=80)

login_btn = tk.Button(main_frame, text='Login', bg='khaki', fg='brown', font=('arial', 10, 'bold'), command=login).pack()

delete_btn = tk.Button(main_frame, text='Delete', bg='khaki', fg='brown', font=('arial', 10, 'bold'), command=delete)
delete_btn.place(x=350, y=80)

tree = ttk.Treeview(main_frame, columns=('username', 'password'), show='headings')
tree.column('username', anchor='center', stretch='NO')
tree.heading('username', text='Username')
tree.column('password', anchor='center', stretch='NO')
tree.heading('password', text='Password')
tree.pack(pady=10)
window.mainloop()