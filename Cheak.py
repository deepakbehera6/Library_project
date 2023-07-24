from tkinter import *
from PIL import ImageTk,Image
import pandas as pd
from tkinter import messagebox
import pymysql
def cheak():  
    root=Tk()
    root.title("Cheak the book")
    root.geometry("1230x520+310+160")
    title=Label(root,bg="gold",fg="silver")
    title.place(x=0,y=0,width=1600,height=800)
    
   
    conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
    curobj=conobj.cursor()
    curobj.execute('use library;')
    curobj.execute('select * from restbook;')
    data=curobj.fetchall()
    
    curobj.execute('select * from user;')
    data1=curobj.fetchall()
  
    
    for i in data:
        pass
    m=list(i)
    
    for x in data1:
        pass
    k=list(x)
 
    myindex=['    username      ','    userid          ','     sem            ','    branch      ','    book1       ','    book2       ','    book3       ','    book4       ','    book5       ']
    mycolumn=["Books"]
    mydata=[m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8]]
    mydata1=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8]]
    
    df=pd.DataFrame(data=mydata,index=myindex,columns=mycolumn)
    
    df1=pd.DataFrame(data=mydata1,index=myindex,columns=mycolumn)
    
    #print(df)
   
    abc=df[df["Books"]!=df1["Books"]]
    
   
    
    labe1=Label(root, text=df1,bg="green",fg='black',font=("bold",15),height=12,width=80)
    labe1.pack()
    
    

    
    title=Label(root,text="User Information",font=("time new roman",20,"bold"),bg="gold",fg="red",relief=RAISED,borderwidth=10)
    title.place(x=170,y=0,width=890,height=50)
    
    
    labe1=Label(root, text=abc,bg="red",fg='black',font=("bold",15),height=10,width=80)
    labe1.pack()
    
    title=Label(root,text="Book Already Returned",font=("time new roman",20,"bold"),bg="gold",fg="red",relief=RAISED,borderwidth=10)
    title.place(x=170,y=258,width=890,height=50)
    
   
   
    
    
    root.mainloop()
#cheak()