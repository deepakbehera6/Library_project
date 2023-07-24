from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from Cheak import*
import pymysql
def search():
    a=userid.get()
    b=sem.get()
    c=branch.get()
    if a=="" or b=="" or c=="":
        messagebox.showerror("","Please enter the information")
    conobj=pymysql.connect(host="localhost",user="root",password="")
    curobj=conobj.cursor()
    curobj.execute("use library;")
   
    conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
    curobj=conobj.cursor()
    curobj.execute('use library;')
    
    curobj.execute("select userid,sem,branch from restbook")
    record=curobj.fetchall()
    for u,v,w in record:
        
        if u==a and v==b and w==c:
            cheak()
            break
    if a not in record and b not in record and c not in record:
        messagebox.showerror("","please enter the valid information")
            
    curobj.execute("select book1,book2,book3,book4,book5  from user where userid='" +a+ "' ")
    show=curobj.fetchall()
    for one,two,three,four,five in show:
        pass
    if one=="" and two=="" and three=="" and four=="" and five=="":
        curobj.execute('delete from user where userid="' +a+ '"')
        curobj.execute('delete from restbook where userid="' +a+ '"')
        
        curobj.execute('commit;')
     
            

    conobj.commit()
    curobj.close()
    conobj.close()
    
def status(): 
    global userid,sem,branch,root
    root=Tk()
    root.title("library")
    root.geometry("1230x520+310+160")
    title=Label(root,bg="gold",fg="silver")
    title.place(x=0,y=0,width=1600,height=800)
    
   
    title1=Label(root,text="User Status Show Here",font=("time new roman",40,"bold"),bg="Black",fg="gold")
    title1.place(x=-150,y=0,width=1600,height=50)
    la1=Label(root,text="User Id :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=75,height=40,width=200)
   
    userid=Entry(root)
    userid.place(x=600,y=75,height=30,width=300)
   
    la1=Label(root,text="Semester :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=110,height=40,width=200)
       
    sem=Entry(root)
    sem.place(x=600,y=110,height=30,width=300)
   
    la1=Label(root,text="Branch :",bg="gold",fg="black",font=("time new roman",20))
    la1.place(x=300,y=145,height=40,width=200)
       
    branch=Entry(root)
    branch.place(x=600,y=145,height=30,width=300)
    
    
     
    submit=Button(root,text="submit",bg="Black",fg="gold",font=("time new roman",10),borderwidth=10,command=search)
    submit.place(x=400,y=225,height=50,width=100)
    
    cancel=Button(root,text="Quit",bg="black",fg="gold",font=("time new roman",10),command=root.destroy,borderwidth=10)
    cancel.place(x=600,y=225,height=50,width=100)
    
    root.mainloop()
#status()