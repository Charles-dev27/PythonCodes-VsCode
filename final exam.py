import tkinter as tk
from tkinter import ttk, messagebox


def data():
    global current_index
    student_name = entry1.get()
    student_id = entry2.get()

    if not student_name.isalpha():
        messagebox.showerror('Invalid Input', 'Student name cant be empty or integer')
        return

    tree.insert('', 'end', values=(current_index, student_name, student_id))
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    current_index += 1

def delete():
    selected = tree.selection()
    if selected:
        tree.delete(selected)

window = tk.Tk()
window.title('Final Exam')
window.config(bg='khaki')


current_index =1

#frame for labels
label_frame = tk.LabelFrame(window,text='Add Student', fg='Orange', bg='Khaki', font=('Bahnscrift', 15,), padx=20, pady=50)
label_frame.pack()

#labels
label = tk.Label(label_frame, text='Student Name', fg='blue', bg='Khaki')
label.grid(row=0, column=0, padx=10)

label2 = tk.Label(label_frame, text='Student Id', fg='blue', bg='Khaki')
label2.grid(row=1, column=0, padx=10)

#entry
entry1 = tk.Entry(label_frame)
entry1.grid(row=0, column=1, padx=10)

entry2 = tk.Entry(label_frame)
entry2.grid(row=1, column=1, padx=10)

#frame for tree view
tree_frame = tk.LabelFrame(window,text='Add Student', fg='Orange', bg='Khaki', font=('Bahnscrift', 15,), padx=20, pady=20)
tree_frame.pack(padx=30, pady=10)

tree =ttk.Treeview(tree_frame, columns=['index', 'student name', 'student id'], show='headings', cursor='hand2')
tree.heading('index', text='#')
tree.heading('student name', text='Student Name')
tree.heading('student id', text='Student Id')
tree.pack()

#buttons
btn1 = tk.Button(label_frame, text='Delete', fg='blue', bg='orange', command=delete)
btn1.place(x=150, y=50)

btn2 = tk.Button(label_frame, text='Add',  fg='blue', bg='orange', command=data)
btn2.place(x=203, y=50)


window.mainloop()