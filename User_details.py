from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from Add import *

def userinfo():
    a=username.get()
    b=userid.get()
    m=sem.get()
    n=branch.get()
    c=book1.get()
    d=book2.get()
    e=book3.get()
    f=book4.get()
    g=book5.get()
    one=''
    two=''
    three=''
    four=''
    five=''
    conobj=pymysql.connect(host="localhost",user="root",password="")
    curobj=conobj.cursor()
    curobj.execute("use library;")
    
    curobj.execute("select bookname from book;")
    record=curobj.fetchall()
    for book in record:
        if c in book:
            one=c
        if d in book:
            two=d
        if e in book:
           three=e
        if f in book:
            four=f
        if g in book:
            five=g
    
    curobj.execute('insert into restbook values("' +a+ '","' +b+ '","' +m+ '","' +n+ '","' +one+ '","' +two+ '","' +three+ '","' +four+ '","' +five+ '")')
    curobj.execute('insert into user values("' +a+ '","' +b+ '","' +m+ '","' +n+ '","' +one+ '","' +two+ '","' +three+ '","' +four+ '","' +five+ '")')
    messagebox.showinfo("","Information is added successfullly...")
    conobj.commit()
    curobj.close()
    conobj.close() 
    root.destroy()
def user():
    
    global bookname,username,userid,book1,book2,book3,book4,book5,root,sem,branch
    root=Tk()
    root.title("library")
    root.geometry("1200x590+330+90")
    title=Label(root,bg="gold",fg="silver")
    title.place(x=0,y=0,width=1200,height=700)
     
    
    
   
    title1=Label(root,text="Add User Information",font=("time new roman",40,"bold"),bg="Black",fg="gold")
    title1.place(x=-150,y=0,width=1600,height=50)
    
    la1=Label(root,text="Name :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=75,height=40,width=200)
    
    username=Entry(root)
    username.place(x=600,y=75,height=30,width=300)
    
    la1=Label(root,text="User Id :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=110,height=40,width=200)
    
    userid=Entry(root)
    userid.place(x=600,y=110,height=30,width=300)
    
    la1=Label(root,text="Semester :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=145,height=40,width=200)
    
    sem=Entry(root)
    sem.place(x=600,y=145,height=30,width=300)
    
    la1=Label(root,text="Branch :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=180,height=40,width=200)
    
    branch=Entry(root)
    branch.place(x=600,y=180,height=30,width=300)
    
    la1=Label(root,text="Book1 :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=215,height=40,width=200)
    
    book1=Entry(root)
    book1.place(x=600,y=215,height=30,width=300)
    
    la1=Label(root,text="Book2 :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=250,height=40,width=200)
    
    book2=Entry(root)
    book2.place(x=600,y=250,height=30,width=300)
    
    la1=Label(root,text="Book3 :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=285,height=40,width=200)
    
    book3=Entry(root)
    book3.place(x=600,y=285,height=30,width=300)
    
    la1=Label(root,text="Book4 :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=320,height=40,width=200)
    
    book4=Entry(root)
    book4.place(x=600,y=320,height=30,width=300)
    
    la1=Label(root,text="Book5 :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=355,height=40,width=200)
    
    book5=Entry(root)
    book5.place(x=600,y=355,height=30,width=300)
    
    
    
    
    
    submit=Button(root,text="submit",bg="Black",fg="gold",font=("time new roman",10),borderwidth=10,command=userinfo)
    submit.place(x=400,y=415,height=50,width=100)
    
    cancel=Button(root,text="Quit",bg="black",fg="gold",font=("time new roman",10),command=root.destroy,borderwidth=10)
    cancel.place(x=600,y=415,height=50,width=100)
    
   
       
    root.mainloop()



