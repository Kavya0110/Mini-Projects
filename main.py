from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

top = Tk()
top.geometry('500x400+10+0')
top.title("Calculator")


def save():
    messagebox.showinfo("Your details have been saved")


h1 = Label(top, text="Register Here", fg="#000080", font=("Comic Sans MS", 25, "bold")).place(x=50, y=20)
h2 = Label(top, text="First Name").place(x=50, y=70)
e2 = Entry(top, bg="grey", width=25).place(x=50, y=90)

h3 = Label(top, text="Contact No.").place(x=50, y=120)
e3 = Entry(top, bg="grey", width=25).place(x=50, y=140)

h4 = Label(top, text="Password").place(x=50, y=170)
e4 = Entry(top, bg="grey", show="*", width=25).place(x=50, y=190)

h5 = Label(top, text="Confirm Password").place(x=50, y=220)
e5 = Entry(top, bg="grey", show="*", width=25).place(x=50, y=240)

h6 = Label(top, text="Last Name").place(x=250, y=70)
e6 = Entry(top, bg="grey", width=25).place(x=250, y=90)

h7 = Label(top, text="Email").place(x=250, y=120)
e7 = Entry(top, bg="grey", width=25).place(x=250, y=140)

h8 = Label(top, text="Answer").place(x=250, y=170)
e8 = Entry(top, bg="grey", width=25).place(x=250, y=190)

b1 = Button(top, text="REGISTER NOW ---->", command=save, bg="#000080", fg="white", width=20,
            font=("Comic Sans MS", 8)).place(x=250, y=235)
c1 = Checkbutton(top, text="I Agree The Terms & Conditions", font=("Arial", 5, "bold")).place(x=245, y=215)

h9 = Label(top, text="Already A User?").place(x=250, y=263)
b2 = Button(top, text="Sign In", bg="#000080", fg="white", width=20, font=("Comic Sans MS", 8)).place(x=250, y=283)

quest = ttk.Combobox(top, text="Question")
quest["values"] = ("Select", "Name of Pet", "Name of School", "Place of Birth")
quest.place(x=50, y=280)
quest.current(0)

spinl = Label(top, text="What is your age: ").place(x=50, y=310)
spinbox = Spinbox(top, from_=1, to=20).place(x=50, y=340)
lb1 = Listbox(top)
lb1.insert(1,"Java")
lb1.insert(2,"India")
lb1.insert(3,"python")
lb1.insert(4,"europe")
lb1.place(x=50, y=370)
scroll = Scrollbar(top)
scroll.pack(SIDE="RIGHT", fill = Y)




# email = Label(top, text="Email", fg="blue").place(x=50, y=110)
# password = Label(top, text="Password", fg="blue").place(x=50, y=140)
# e3 = Entry(top, bg="yellow").place(x=150, y=110)
# e4 = Entry(top, show="*", bg="yellow").place(x=150, y=140)

# button2 = Button(top, text='Submit').place(x=50, y=170)


top.mainloop()
