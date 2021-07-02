import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

top = Tk()
top.geometry('400x350+10+10')
top.title("Form")



l1 = Label(top, text="Enter Email id").place(x=20, y=20)
e1 = Entry(top).place(x=20, y=40)

l2 = Label(top, text="Enter Password").place(x=20, y=70)
e2 = Entry(top).place(x=20, y=90)

lbe = Label(top, text="What OS is being used").place(x=20, y=120)
lb1 = Listbox(top)
lb1.insert(1,"Windows")
lb1.insert(2,"Mac OS")
lb1.insert(3,"Linux")
lb1.insert(4,"Android")
lb1.place(x=20, y=140)

ls = Label(top, text="What is Your Age").place(x=200, y=20)
sp1 = Spinbox(top, from_=1, to=20).place(x=200, y=40)
quest = ttk.Combobox(top, text="Question")
quest["values"] = ("Select", "Name of Pet", "Name of School", "Place of Birth")
quest.place(x=200, y=70)
quest.current(0)

check = Checkbutton(top, text="I agree to the terms and conditions").place(x=195, y=100)

submit = Button(top, text="Submit").place(x=200, y=130)

menubar = Menubutton(top, text="courses", relief=RAISED)
menubar.place(x=0, y=0)
menubar.menu=Menu(menubar, tearoff=0)
menubar["menu"] = menubar.menu
pythonvar = IntVar()
javavar = IntVar()
phpvar = IntVar()
menubar.menu.add_checkbutton(label="Python", variable=pythonvar)
menubar.menu.add_checkbutton(label="Java", variable=javavar)
menubar.menu.add_checkbutton(label="Php", variable=phpvar)

menubar = Menubutton(top, text="File", relief=RAISED)
menubar.place(x=52, y=0)
menubar.menu=Menu(menubar, tearoff=0)
menubar["menu"] = menubar.menu
new = IntVar()
Open = IntVar()
save = IntVar()
save_as = IntVar()
menubar.menu.add_checkbutton(label="New", variable=new)
menubar.menu.add_checkbutton(label="Open", variable=Open)
menubar.menu.add_checkbutton(label="Save", variable=save)
menubar.menu.add_checkbutton(label="Save As", variable=save_as) 



top.config(menu=menubar)
top.mainloop()