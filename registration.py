#pip install mysql
import mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector as mysql
#connection for phpmyadmin
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
ph9 = tk.StringVar()

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
    if num ==9:
        ph9.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registration")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    id = str(idEntry.get())
    codigo = str(codigoEntry.get())
    data_inicio = str(data_inicioEntry.get())
    nome_projeto = str(nome_projetoEntry.get())
    tipo = str(tipoEntry.get())
    techs = str(techsEntry.get())
    status_ = str(status_Entry.get())
    notas = str(notasEntry.get())
    data_conclusao = str(data_conclusaoEntry.get())

    if (id == "" or id == " ") or (data_inicio == "" or data_inicio == " ") or (nome_projeto == "" or nome_projeto == " ") or (tipo == "" or tipo == " ") or (techs == "" or techs == " ")or (status_ == "" or status_ == " ")or (notas == "" or notas == " ")or (data_conclusao == "" or data_conclusao == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO registration VALUES ('"+id+"','"+codigo+"','"+data_inicio+"','"+nome_projeto+"','"+tipo+"','"+techs+"','"+status_+"','"+notas+"','"+data_conclusao+"')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
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
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM registration WHERE codigo='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        id = str(my_tree.item(selected_item)['values'][0])
        codigo = str(my_tree.item(selected_item)['values'][1])
        data_inicio = str(my_tree.item(selected_item)['values'][2])
        nome_projeto = str(my_tree.item(selected_item)['values'][3])
        tipo = str(my_tree.item(selected_item)['values'][4])
        techs = str(my_tree.item(selected_item)['values'][5])
        status_ = str(my_tree.item(selected_item)['values'][6])
        notas = str(my_tree.item(selected_item)['values'][7])
        data_conclusao = str(my_tree.item(selected_item)['values'][8])
        
        setph(id,1)
        setph(codigo,2)
        setph(data_inicio,3)
        setph(nome_projeto,4)
        setph(tipo,5)
        setph(techs,7)
        setph(status_,8)
        setph(notas,9)
        setph(data_conclusao,10)

    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    id = str(idEntry.get())
    codigo = str(codigoEntry.get())
    data_inicio = str(data_inicioEntry.get())
    nome_projeto = str(nome_projetoEntry.get())
    tipo = str(tipoEntry.get())
    techs = str(techsEntry.get())
    status_ = str(status_Entry.get())
    notas = str(notasEntry.get())
    data_conclusao = str(data_conclusaoEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registration WHERE codigo='"+
    codigo+"' or data_inicio='"+
    data_inicio+"' or nome_projeto='"+
    nome_projeto+"' or tipo='"+
    tipo+"' or techs='"+
    techs+"' or status_='"+
    status_+"' or notas='"+
    notas+"' or data_conclusao='"+
    data_conclusao+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,9):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    id = str(idEntry.get())
    codigo = str(codigoEntry.get())
    data_inicio = str(data_inicioEntry.get())
    nome_projeto = str(nome_projetoEntry.get())
    tipo = str(tipoEntry.get())
    techs = str(techsEntry.get())
    status_ = str(status_Entry.get())
    notas = str(notasEntry.get())
    data_conclusao = str(data_conclusaoEntry.get())

    if (id == "" or id == " ") or (data_inicio == "" or data_inicio == " ") or (nome_projeto == "" or nome_projeto == " ") or (tipo == "" or tipo == " ") or (techs == "" or techs == " ")or (status_ == "" or status_ == " ")or (notas == "" or notas == " ")or (data_conclusao == "" or data_conclusao == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM registration WHERE id='"+
            id+"' or codigo='"+
            codigo+"' or data_inicio='"+
            data_inicio+"' or nome_projeto='"+
            nome_projeto+"' or tipo='"+
            tipo+"' or techs='"+
            techs+"' or status_='"+
            status_+"' or notas='"+
            notas+"' or data_conclusao='"+
            data_conclusao+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()

label = Label(root, text=" Project Registration System ", font=('Arial Bold', 35))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

idLabel = Label(root, text="id", font=('Arial', 20))
codigoLabel = Label(root, text="codigo", font=('Arial', 20))
data_inicioLabel = Label(root, text="data_incio", font=('Arial', 20))
nome_projetoLabel = Label(root, text="nome_projeto", font=('Arial', 20))
tipoLabel = Label(root, text="tipo", font=('Arial', 20))
techsLabel = Label(root, text="techs", font=('Arial', 20))
status_Label = Label(root, text="status_", font=('Arial', 20))
notasLabel = Label(root, text="notas", font=('Arial', 20))
data_conclusaoLabel = Label(root, text="data_conclusao", font=('Arial', 20))


idLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
codigoLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
data_inicioLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
nome_projetoLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
tipoLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)
techsLabel.grid(row=8, column=0, columnspan=1, padx=50, pady=5)
status_Label.grid(row=9, column=0, columnspan=1, padx=50, pady=5)
notasLabel.grid(row=10, column=0, columnspan=1, padx=50, pady=5)
data_conclusaoLabel.grid(row=11, column=0, columnspan=1, padx=50, pady=5)

idEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
codigoEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
data_inicioEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
nome_projetoEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
tipoEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)
techsEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph6)
status_Entry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph7)
notasEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph8)
data_conclusaoEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable =ph9)

idEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
codigoEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
data_inicioEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
nome_projetoEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
tipoEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
techsEntry.grid(row=8, column=1, columnspan=4, padx=5, pady=0)
status_Entry.grid(row=9, column=1, columnspan=4, padx=5, pady=0)
notasEntry.grid(row=10, column=1, columnspan=4, padx=5, pady=0)
data_conclusaoEntry.grid(row=11, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), background="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), bg="#F4FE82", command=search)
#resetBtn = Button(
   # root, text="Reset", padx=65, pady=25, width=10,
    #bd=5, font=('Arial', 18), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 18), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
#resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=11, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 18))

my_tree['columns'] = ("id","codigo","data_inicio","nome_projeto","tipo","techs","status_","notas","data_conclusao")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("id", anchor=W, width=100)
my_tree.column("codigo", anchor=W, width=100)
my_tree.column("data_inicio", anchor=W, width=150)
my_tree.column("nome_projeto", anchor=W, width=300)
my_tree.column("tipo", anchor=W, width=165)
my_tree.column("techs", anchor=W, width=150)
my_tree.column("status_", anchor=W, width=150)
my_tree.column("notas", anchor=W, width=150)
my_tree.column("data_conclusao", anchor=W, width=150)

my_tree.heading("id", text="ID", anchor=W)
my_tree.heading("codigo", text="Codigo", anchor=W)
my_tree.heading("data_inicio", text="Data Inicio", anchor=W)
my_tree.heading("nome_projeto", text="Nome Projeto", anchor=W)
my_tree.heading("tipo", text="Tipo", anchor=W)
my_tree.heading("techs", text="Techs", anchor=W)
my_tree.heading("status_", text="Status_", anchor=W)
my_tree.heading("notas", text="Notas", anchor=W)
my_tree.heading("data_conclusao", text="Data Conclusao", anchor=W)

refreshTable()

root.mainloop()