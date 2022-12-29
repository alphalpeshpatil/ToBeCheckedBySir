from tkinter import *
root=Tk()
root.geometry("500x300")

Label(root,text="Registration Form",font="arial 15 bold").grid(row=0,column=3)
name=Label(root,text="Name")
LastName=Label(root,text="Last name")
Password=Label(root,text="password")
Email=Label(root,text="email")

name.grid(row=1,column=2)
LastName.grid(row=2,column=2)
Password.grid(row=3,column=2)
Email.grid(row=4,column=2)

nameValue=StringVar
nameValue=StringVar
nameValue=StringVar
nameValue=StringVar 

root.mainloop()