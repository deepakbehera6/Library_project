from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
def register():
    
    a=bookid.get()
    
    conobj=pymysql.connect(host="localhost",user="root",password="")
    curobj=conobj.cursor()
    curobj.execute("use library;")
   
    conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
    curobj=conobj.cursor()
    curobj.execute('use library;')
    
    if curobj.execute("delete from book where bookid = '" +a+ "' "):
        messagebox.showinfo("","Successfully deleted")
   
    else:
        messagebox.showerror("","Plesse enter correct Bookid")
   
    conobj.commit()
    curobj.close()
    conobj.close()
    bookid.delete(0,END)
    root.destroy()
def delete():
    global root
    global bookid;
    root=Tk()
    root.title("library")
    root.geometry("1230x520+310+160")
      
    title=Label(root,bg="gold",fg="silver")
    title.place(x=0,y=0,width=1600,height=800)
    
    title1=Label(root,text="Delete Book Here",font=("time new roman",40,"bold"),bg="Black",fg="gold")
    title1.place(x=-150,y=0,width=1600,height=60)
    
    labelframe=Frame(root,bg="black")
    labelframe.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.5)
    
    la1=Label(labelframe,text="Book Id :",bg="black",fg="white",font=("time new roman",15))
    la1.place(relx=0.05,rely=0.4,relheight=0.1)
    
    bookid=Entry(labelframe)
    bookid.place(relx=0.3,rely=0.4,relheight=0.1,relwidth=0.62)
    
    
    submit=Button(root,text="Delete",bg="Black",fg="gold",font=("time new roman",15),borderwidth=10,command=register)
    submit.place(relx=0.28,rely=0.83,relwidth=0.18,relheight=0.08)
    
    cancel=Button(root,text="Quit",bg="black",fg="gold",font=("time new roman",15),command=root.destroy,borderwidth=10)
    cancel.place(relx=0.53,rely=0.83,relwidth=0.18,relheight=0.08)
    
    
    
    
    root.mainloop()
