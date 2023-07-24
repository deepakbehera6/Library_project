from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
def bookreturn():
    a=userid.get()
    b=book.get()
    
    
    conobj=pymysql.connect(host="localhost",user="root",password="")
    curobj=conobj.cursor()
    curobj.execute("use library;")
   
    conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
    curobj=conobj.cursor()
    curobj.execute('use library;')
    '''if curobj.execute("delete from user where userid = '" +a+ "' "):
        messagebox.showinfo("Return","Return book successfully")
    else:
        messagebox.showerror("","Enter the correct userid")'''
    if a=="" or b=="":
        
        messagebox.showerror("","Entrer User id and book you havae to return")
    elif curobj.execute("select book1,book2,book3,book4,book5  from user where userid='" +a+ "' "):
        show=curobj.fetchall()
    
        for i in show:
            pass
          
        
        m=list(i)
        n=m.index(b)
        m[n]=''
        for s in m:
            one=m[0]
            two=m[1]
            three=m[2]
            four=m[3]
            five=m[4]
       

        curobj.execute('update user set book1="' +one+ '",book2="' +two+ '",book3="' +three+ '",book4="' +four+ '",book5="' +five+ '";')
    
    else:
        messagebox.showerror("","enter correct user id")
        
            
   
    conobj.commit()
    curobj.close()
    conobj.close()
    userid.delete(0,END)
    root.destroy()

def return1():
    global userid,root,book;
    root=Tk()
    root.title("library")
    root.geometry("1230x520+310+160")
      
    title=Label(root,bg="gold",fg="silver")
    title.place(x=0,y=0,width=1600,height=800)
    
    title1=Label(root,text="Return Book Here",font=("time new roman",40,"bold"),bg="Black",fg="gold")
    title1.place(x=-150,y=0,width=1600,height=60)
    
    labelframe=Frame(root,bg="black")
    labelframe.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.5)
    
    la1=Label(labelframe,text="User Id: " ,bg="black",fg="white",font=("time new roman",15))
    la1.place(relx=0.05,rely=0.4,relheight=0.1)
    
    userid=Entry(labelframe)
    userid.place(relx=0.3,rely=0.4,relheight=0.1,relwidth=0.62)
    
    la1=Label(labelframe,text="Book Name : " ,bg="black",fg="white",font=("time new roman",15))
    la1.place(relx=0.05,rely=0.7,relheight=0.1)
    
    book=Entry(labelframe)
    book.place(relx=0.3,rely=0.7,relheight=0.1,relwidth=0.62)
    
    
    submit=Button(root,text="Return",bg="Black",fg="gold",font=("time new roman",15),borderwidth=10,command=bookreturn)
    submit.place(relx=0.28,rely=0.83,relwidth=0.18,relheight=0.08)
    
    cancel=Button(root,text="Quit",bg="black",fg="gold",font=("time new roman",15),command=root.destroy,borderwidth=10)
    cancel.place(relx=0.53,rely=0.83,relwidth=0.18,relheight=0.08)
    
    
    
    
    root.mainloop()
#return1()