#pip install mysql
import mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector as mysql

#connection for MySql
def connection():
    conn = mysql.connect(
        host='localhost',
        port='8889',
        user='root', 
        password='root',
        database='db_ProjectRegistration',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=58, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Project Registration System")
root.geometry("1920x1080")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()
ph8 = tk.StringVar()


#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)
    if num ==6:
        ph6.set(word)
    if num ==7:
        ph7.set(word)
    if num ==8:
        ph8.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registration")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    code = str(codeEntry.get())
    start_date = str(start_dateEntry.get())
    project_name = str(project_nameEntry.get())
    project_type = str(project_typeEntry.get())
    technologies = str(technologiesEntry.get())
    status_ = str(status_Entry.get())
    annotations = str(annotationsEntry.get())
    completion_date = str(completion_dateEntry.get())

    if (code == "" or code == " ") or (start_date == "" or start_date == " ") or (project_name == "" or project_name == " ") or (project_type == "" or project_type == " ") or (technologies == "" or technologies == " ") or (status_ == "" or status_ == " ") or (annotations == "" or annotations == " ") or (completion_date == "" or completion_date == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO registration VALUES ('"+code+"','"+start_date+"','"+project_name+"','"+project_type+"','"+technologies+"','"+status_+"','"+annotations+"','"+completion_date+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Project Code already exist")
            return

    refreshTable()
    
def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM registration")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['VALUES'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM registration WHERE code='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        code = str(my_tree.item(selected_item)['values'][0])
        start_date = str(my_tree.item(selected_item)['values'][1])
        project_name = str(my_tree.item(selected_item)['values'][2])
        project_type = str(my_tree.item(selected_item)['values'][3])
        technologies = str(my_tree.item(selected_item)['values'][4])
        status_ = str(my_tree.item(selected_item)['values'][5])
        annotations = str(my_tree.item(selected_item)['values'][6])
        completion_date = str(my_tree.item(selected_item)['values'][7])
        
        setph(code,1)
        setph(start_date,2)
        setph(project_name,3)
        setph(project_type,4)
        setph(technologies,5)
        setph(status_,6)
        setph(annotations,7)
        setph(completion_date,8)

    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    code = str(codeEntry.get())
    start_date = str(start_dateEntry.get())
    project_name = str(project_nameEntry.get())
    project_type = str(project_typeEntry.get())
    technologies = str(technologiesEntry.get())
    status_ = str(status_Entry.get())
    annotations = str(annotationsEntry.get())
    completion_date = str(completion_dateEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registration WHERE code='"+
    code+"' or start_date='"+
    start_date+"' or project_name='"+
    project_name+"' or project_type='"+
    project_type+"' or technologies='"+
    technologies+"' or status_='"+
    status_+"' or annotations='"+
    annotations+"' or completion_date='"+
    completion_date+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,8):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedcode = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedcode = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    code = str(codeEntry.get())
    start_date = str(start_dateEntry.get())
    project_name = str(project_nameEntry.get())
    project_type = str(project_typeEntry.get())
    technologies = str(technologiesEntry.get())
    status_ = str(status_Entry.get())
    annotations = str(annotationsEntry.get())
    completion_date = str(completion_dateEntry.get())

    if (code ==""or code== " ")or(start_date == "" or start_date == " ") or (project_name == "" or project_name == " ") or (project_type == "" or project_type == " ") or (technologies == "" or technologies == " ") or (status_ == "" or status_ == " ") or (annotations == "" or annotations == " ") or (completion_date == "" or completion_date == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "Update registration SET code='"+
                code+"' , start_date='"+
                start_date+"' , project_name='"+
                project_name+"' , project_type='"+
                project_type+"' , technologies='"+
                technologies+"' , status_='"+
                status_+"' , annotations='"+
                annotations+"' , completion_date='"+
                completion_date+"' WHERE code='"+
                selectedcode + "' "
            )
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Project code already exist")
            return

    refreshTable()

label = Label(root, text=" Project Registration System ", font=('Arial Bold', 35))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

codeLabel = Label(root, text="Code", font=('Arial', 20))
start_dateLabel = Label(root, text="Start Date", font=('Arial', 20))
project_nameLabel = Label(root, text="Project Name", font=('Arial', 20))
project_typeLabel = Label(root, text="Type", font=('Arial', 20))
technologiesLabel = Label(root, text="Technologies", font=('Arial', 20))
status_Label = Label(root, text="Status", font=('Arial', 20))
annotationsLabel = Label(root, text="Annotations", font=('Arial', 20))
completion_dateLabel = Label(root, text="Date Conclusion", font=('Arial', 20))


codeLabel.grid(row=4, column=0, columnspan=2, padx=50, pady=5)
start_dateLabel.grid(row=5, column=0, columnspan=2, padx=50, pady=5)
project_nameLabel.grid(row=6, column=0, columnspan=2, padx=50, pady=5)
project_typeLabel.grid(row=7, column=0, columnspan=2, padx=50, pady=5)
technologiesLabel.grid(row=8, column=0, columnspan=2, padx=50, pady=5)
status_Label.grid(row=9, column=0, columnspan=2, padx=50, pady=5)
annotationsLabel.grid(row=10, column=0, columnspan=2, padx=50, pady=5)
completion_dateLabel.grid(row=11, column=0, columnspan=2, padx=50, pady=5)

codeEntry = Entry(root,width=55, bd=5, font=('Arial', 15), textvariable = ph1)
start_dateEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
project_nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
project_typeEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
technologiesEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)
status_Entry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph6)
annotationsEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph7)
completion_dateEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable =ph8)

codeEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
start_dateEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
project_nameEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
project_typeEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
technologiesEntry.grid(row=8, column=1, columnspan=4, padx=5, pady=0)
status_Entry.grid(row=9, column=1, columnspan=4, padx=5, pady=0)
annotationsEntry.grid(row=10, column=1, columnspan=4, padx=5, pady=0)
completion_dateEntry.grid(row=11, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18),  command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18),  command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 14))

my_tree['columns'] = ("code", "start_date", "project_name", "project_type", "technologies", "status_", "annotations", "completion_date")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("code", anchor=W, width=80)
my_tree.column("start_date", anchor=W, width=100)
my_tree.column("project_name", anchor=W, width=250)
my_tree.column("project_type", anchor=W, width=80)
my_tree.column("technologies", anchor=W, width=150)
my_tree.column("status_", anchor=W, width=150)
my_tree.column("annotations", anchor=W, width=300)
my_tree.column("completion_date", anchor=W, width=120)

my_tree.heading("code", text="Code", anchor=W)
my_tree.heading("start_date", text="Start Date", anchor=W)
my_tree.heading("project_name", text="Project Name", anchor=W)
my_tree.heading("project_type", text="Type", anchor=W)
my_tree.heading("technologies", text="Technologies", anchor=W)
my_tree.heading("status_", text="Status", anchor=W)
my_tree.heading("annotations", text="Annotations", anchor=W)
my_tree.heading("completion_date", text="Date Conclusion", anchor=W)

refreshTable()

root.mainloop()