import tkinter as tk
from tkinter import ttk

def insert_data():
    global current_index
    student_name = entry1.get()
    student_id = entry2.get()
    if student_name and student_id:
        treeview.insert("", "end", values=(current_index, student_name, student_id))
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        current_index += 1
        save_data(student_name, student_id)

def delete_data():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)


def save_data(name, id):
    with open("student_data.txt", "a") as file:
        file.write(f"{name},{id}\n")


window = tk.Tk()
window.geometry('670x500')
window.configure(bg='khaki') 

current_index = 1

lbl_frame = tk.LabelFrame(window, text='Add Students', foreground='purple', background='khaki', padx=10, pady=10, font=('bold', 10))
lbl_frame.pack(padx=10, pady=10)

add_student = tk.Label(lbl_frame, text='Student Name', fg='purple', bg='khaki', pady=5)
add_student.grid(row=0, column=0)

entry1 = tk.Entry(lbl_frame)
entry1.grid(row=0, column=1)

add_student_id = tk.Label(lbl_frame, text='Student ID', foreground='purple', background='khaki', pady=5)
add_student_id.grid(row=1, column=0)

entry2 = tk.Entry(lbl_frame)
entry2.grid(row=1, column=1, padx=25)

btn = tk.Button(lbl_frame, text='Add', bg='orange', fg='purple', pady=5, command=insert_data)
btn.place(x=100, y=60)

btn2 = tk.Button(lbl_frame, text='Delete', bg='orange', fg='purple', pady=5, command=delete_data)
btn2.grid(row=2, column=1)


treeview_frame = tk.LabelFrame(window, text='Students Lists', font=('arial', 10), fg='purple', bg='khaki')
treeview_frame.pack(padx=30, pady=10)
column = ('index', 'Student Name', 'Student ID')

sort_frame = tk.LabelFrame(window, text='Students Lists', font=('arial', 10), fg='purple', bg='khaki')
sort_frame.pack(side='right', padx=30, pady=10)


treeview = ttk.Treeview(treeview_frame, columns=column, show='headings')
treeview.heading('index', text='#')
treeview.heading('Student Name', text='Student Name')
treeview.heading('Student ID', text='Student ID')
treeview.grid(row=0, column=0)

window.mainloop()