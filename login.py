import tkinter as tk
from tkinter import messagebox

def pass_validation():
    pass

window = tk.Tk()
window.title('Login')
window.config(bg='Khaki')
window.geometry('440x440')

main_frame = tk.LabelFrame(window, text='Login Form', font=('arial', 15), fg='purple', bg='khaki', padx=10, pady=10)
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

login_label = tk.Label(main_frame, text='Username', fg='brown', bg='khaki', font=('arial', 10, 'bold'))
password_valid = tk.StringVar()
password_valid.trace('w', pass_validation) 
login_label.place(x=20, y=30)

user_indicator = tk.Label(main_frame,text='')
user_indicator.place(x=20, y=45)
window.mainloop()