from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def showdetails():
    
    
    root=Tk()
    root.title("library")
    root.geometry("1230x520+310+160")
    title=Label(root,bg="gold",fg="silver")
    title.place(x=0,y=0,width=1600,height=800)
     
   
    conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
    curobj=conobj.cursor()
    curobj.execute('use library;')
    curobj.execute('select * from user;')
    data=curobj.fetchall()
    #labe1=Label(root,text=[i for i in data])
   # x=["Book Id","Book Name","Author"]
    
    
    label=Label(root, text="%-60s%-50s%-40s%-20s"%('User Name','User Id','Semester','Branch'),bg="gold",fg='black',font=("bold",12))
    label1=Label(root, text="---------------------------------------------------------------------------------------------------",bg="gold",fg='black',font=("bold",20))
    label.pack()
    label1.pack()
    for i in data:
       labe1=Label(root, text="%-60s%-50s%-40s%-20s"%(i[0],i[1],i[2],i[3]),bg="gold",fg='black',font=("bold",12))
       labe1.pack()
   
    conobj.commit()
    curobj.close()
    conobj.close()
    
   
       
    root.mainloop()

#showdetails()
