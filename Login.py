from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Library import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("800x600")
root.title("login page")
root.maxsize(height=600,width=800)



img1=Image.open("lib.jpg")
img1=img1.resize((800,600),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(img1)
iblimg=Label(root,image=photoimg1)
iblimg.place(width=800,height=600)

title=Label(root,text="Admin Pannel",font=("time new roman",40,"bold"),bg="gold",fg="red")
title.place(x=0,y=0,width=800,height=60)

user_name=Label(root,text="     user name",font=("time new roman",20,"bold"),fg="white",bg="black")
user_name.place(x=40,y=100)

textuser=ttk.Entry(root,font=("time new roman",15,"bold"))
textuser.place(x=250,y=100,width=270)

password=Label(root,text="     password",font=("time new roman",20,"bold"),fg="white",bg="black")
password.place(x=40,y=225)

textpass=ttk.Entry(root,font=("time new roman",15,"bold"),show="*")
textpass.place(x=250,y=225,width=270)

def login():
   
    if textuser.get()=="" or textpass.get()=="":
        messagebox.showerror("error","Enter the information first")
    elif textuser.get()=="admin" and textpass.get()=="pass":
        root.destroy()
        library()
    else:
        messagebox.showerror("error","Either usernamr or pass word is incorrect")
        textuser.delete(0,END)
        textpass.delete(0,END)
login=Button(root,text="login",font=("times new roman",15,"bold"),command=login,borderwidth=10)
login.place(x=150,y=350,width=160)

login=Button(root,text="cancel",font=("times new roman",15,"bold"),command=root.destroy,borderwidth=10)
login.place(x=370,y=350,width=160)


img5=Image.open("images.jpg")
img5=img5.resize((35,35),Image.ANTIALIAS)
photoimg5=ImageTk.PhotoImage(img5)
iblimg=Label(root,image=photoimg5)
iblimg.place(width=35,height=35,x=40,y=101)

img6=Image.open("pass.png")
img6=img6.resize((35,35),Image.ANTIALIAS)
photoimg6=ImageTk.PhotoImage(img6)
iblimg=Label(root,image=photoimg6)
iblimg.place(width=35,height=35,x=40,y=226)
    
img3=Image.open("submt.png")
img3=img3.resize((38,35),Image.ANTIALIAS)
photoimg3=ImageTk.PhotoImage(img3)
iblimg=Label(root,image=photoimg3)
iblimg.place(width=38,height=35,x=170,y=360)
     
img4=Image.open("cancel.png")
img4=img4.resize((32,30),Image.ANTIALIAS)
photoimg4=ImageTk.PhotoImage(img4)
iblimg=Label(root,image=photoimg4)
iblimg.place(width=32,height=30,x=390,y=360)


        
       

root.mainloop()
