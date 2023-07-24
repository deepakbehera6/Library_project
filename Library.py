from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from Add import *
from Delete import *
from Return import*
from Info import *
from Show_details import *
from User_details import *
from Search_Status import *
import pymysql
def library():
    root=Tk()
    
    root.title("Deepak LIB")
    #root.minsize(width=400,height=400)
    #root.maxsize(height=600,width=400)
    root.geometry("2400x900+0+0")
    
    
    img1=Image.open("lib.jpg")
    img1=img1.resize((500,700),Image.ANTIALIAS)
    #print(img1)
    photoimg1=ImageTk.PhotoImage(img1)
    iblimg=Label(root,image=photoimg1)
    iblimg.place(x=0,y=60,width=310,height=620)
    
    img=Image.open("lib2.jpg")
    img=img.resize((1200,810),Image.ANTIALIAS)
    photoimg=ImageTk.PhotoImage(img)
    iblimg=Label(root,image=photoimg)
    iblimg.place(x=310,y=0,width=1200,height=680)
    
    #title=Label(root,bg="#ab9fbb")
    #title.place(x=0,y=60,width=310,height=620)
    
    
    #title=Label(root,bg="#d5e1df")
    #title.place(x=310,y=0,width=1300,height=680)
    
    
    title1=Label(root,bg="white",bd=4,relief=RIDGE,font=("bold",20))
    title1.place(x=10,y=690,width=1500,height=100)
    
   
    
    
    
    
    title=Label(root,text="Library Management System",font=("time new roman",40,"bold"),bg="gold",fg="red",relief=RAISED,borderwidth=10)
    title.place(x=0,y=0,width=1600,height=75)
    
    
    btn1 = Button(root,text="Add Book",bg='black', fg='gold',command=add,borderwidth=20)
    btn1.place(relx=0.007,rely=0.10,relheight=0.08,relwidth=0.15)
    
    btn2 = Button(root,text="Delete Book",bg='black', fg='gold',command=delete,borderwidth=20)
    btn2.place(relx=0.007,rely=0.20,relheight=0.08,relwidth=0.15)
    
    btn3 = Button(root,text="Show Book",bg='black', fg='gold',borderwidth=20,command=info)
    btn3.place(relx=0.007,rely=0.30,relheight=0.08,relwidth=0.15)
    
    btn4 = Button(root,text="User Details",bg='black', fg='gold',borderwidth=20,command=user)
    btn4.place(relx=0.007,rely=0.40,relheight=0.08,relwidth=0.15)
    
    btn5 = Button(root,text="Show User Information",bg='black', fg='gold',borderwidth=20,command=showdetails)
    btn5.place(relx=0.007,rely=0.50,relheight=0.08,relwidth=0.15)
    
    btn6 = Button(root,text="Return Book",bg='black', fg='gold',borderwidth=20,command=return1)
    btn6.place(relx=0.007,rely=0.60,relheight=0.08,relwidth=0.15)
    
     
    btn7 = Button(root,text="Search Status",bg='black', fg='gold',borderwidth=20,command=status)
    btn7.place(relx=0.007,rely=0.70,relheight=0.08,relwidth=0.15)
    
    
    
    
    root.mainloop()
#library()