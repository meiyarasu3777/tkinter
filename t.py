

from tkinter import *
from PIL import ImageTk, Image

import pymysql

mydb=pymysql.Connection(host="localhost",user="root",password="12345",database="project_mini")
cur=mydb.cursor()
cur.execute("use project_mini")                       
bal=25000
global n,em,acn,pho,psd
w=Tk()
w.title("Frame=1")
w.geometry("1300x700")



img=ImageTk.PhotoImage(Image.open("banner1.jpg"),master=w)
img_label1=Label(w,image=img)
img_label1.place(width=1300,height=700)

def balance():
    global bal,img5
    w5=Tk()
    w5.title("Frames=6")
    w5.geometry("1300x780")
    img5 = ImageTk.PhotoImage(Image.open("banner2.jpg"),master=w5)
    lab26=Label(w5,image=img5)
    lab26.place(width=1300,height=768)
    
    
    l8=Label(w5,text="YOUR BALANCE ",font="bold 20",fg="black")
    l8.place(x=470,y=40)
    l9=Label(w5,text=bal,fg="black")
    l9.place(x=500,y=120)
    b10=Button(w5,text="OK",width=20,fg="white",bg="black")
    b10.place(x=490,y=200)
   
def sub():
    global bal
    data=int(e9.get())
    bal-=data
    print("added successfully:",bal)

def wit():
    global w4,e9,img4
    w4=Tk()
    w4.title("Frame=5")
    w4.geometry("1300x780")
    img4 = ImageTk.PhotoImage(Image.open("banner2.jpg"),master=w4)
    lab25=Label(w4,image=img4)
    lab25.place(width=1300,height=768)
    
    
    l6=Label(w4,text="INDIAN BANK",font=" bold 20",fg="black")
    l6.place(x=470,y=40)
    l7=Label(w4,text="ENTER THE WITHDRAW AMOUNT",fg="black")
    l7.place(x=480,y=100)
    e9=Entry(w4,width=30)
    e9.place(x=480,y=150)
    b9=Button(w4,text="Submit",width=15,fg="white",bg="black",command=sub)
    b9.place(x=480,y=200)

def add():
    global bal
    data=int(e8.get())
    print(data)
    bal+=data
    print("added successfully:",bal)

def dep():
    global w3,e8,img3
    w3=Tk()
    w3.title("Frame=4")
    w3.geometry("1300x780")
    img3 = ImageTk.PhotoImage(Image.open("banner2.jpg"),master=w3)
    lab24=Label(w3,image=img3)
    lab24.place(width=1300,height=768)
    l4=Label(w3,text="INDIAN BANK",font=" bold 20",fg="black")
    l4.place(x=470,y=40)
    l5=Label(w3,text="ENTER THE DEPOSIT AMOUNT",fg="black")
    l5.place(x=480,y=100)
    e8=Entry(w3,width=30)
    e8.place(x=480,y=150)
    b8=Button(w3,text="Submit",width=15,fg="white",bg="black",command=add)
    b8.place(x=480,y=200)

    
def account():
    global w2,img2,a1,p1
    a1=acc.get()
    p1=pwd.get()
    cur.execute("select * from details")
    for i in cur:
        if i[2]==a1 and i[4]==p1:
    
            w2=Tk()
            w2.title("Frame=3")
            w2.geometry("1300x780")
            img2 = ImageTk.PhotoImage(Image.open("banner2.jpg"),master=w2)
            lab23=Label(w2,image=img2)
            lab23.place(width=1300,height=768)
            l3=Label(w2,text="WELCOME!!",font="bold 20",fg="black")
            l3.place(x=470,y=30)
            b5=Button(w2,text="DEPOSIT",width=25,fg="white",bg="black",command=dep)
            b5.place(x=470,y=120)
            b6=Button(w2,text="WITHDRAW",width=25,fg="white",bg="black",command=wit)
            b6.place(x=470,y=180)
            b7=Button(w2,text="CHECK BALANCE",width=25,fg="white",bg="black",command=balance)
            b7.place(x=470,y=240)


           
def log():
    global photo2,Image_lab2,w1,e3,e4,e5,img1,acc,pwd
    n=e1.get()
    em=e2.get()
    acn=e3.get()
    pho=e4.get()
    psd=e5.get()
    query="insert into details values(%s,%s,%s,%s,%s)"
    print("start")
    val=[n,em,acn,pho,psd]
    cur.execute(query,val)
    mydb.commit()
    print("stop")
    w1=Tk()
    w1.title("Frame=2")
    w1.geometry("1300x780")
    
    img1 = ImageTk.PhotoImage(Image.open("banner2.jpg"),master=w1)
    lab22=Label(w1,image=img1)
    lab22.place(width=1300,height=768)
    
    l2=Label(w1,text="LOGIN PAGE",font="bold 25",fg="black")
    l2.place(x=420,y=40)
    n7=Label(w1,text="ACCOUNT NO:",font="bold 10")
    n7.place(x=430,y=120)
    acc=Entry(w1,width=20)
    acc.place(x=540,y=120)
    n8=Label(w1,text="PIN NO:",font="bold 10")
    n8.place(x=430,y=160)
    pwd=Entry(w1,width=20)
    pwd.place(x=540,y=160)
    b3=Button(w1,text="submit",width=10,fg="white",bg="black",command=account)
    b3.place(x=440,y=200)
    b4=Button(w1,text="Exit",width=10,fg="white",bg="black")
    b4.place(x=540,y=200)

           
l=Label(w,text="WELCOME TO INDIAN BANK",fg="black",font="bold 25")
l.place(x=350,y=50)

n1=Label(w,text=" NAME:")
n1.place(x=370,y=130)


e1=Entry(w,width=20)
e1.place(x=490,y=130)

n2=Label(w,text=" EMAIL ID:")
n2.place(x=370,y=160)

e2=Entry(w,width=20)
e2.place(x=490,y=160)

n3=Label(w,text="ACCOUNT NUMBER:")
n3.place(x=370,y=190)

e3=Entry(w,width=20)
e3.place(x=490,y=190)


n4=Label(w,text="PHONE NUMBER:")
n4.place(x=370,y=220)

e4=Entry(w,width=20)
e4.place(x=490,y=220)

n5=Label(w,text=" PASSWORD:")
n5.place(x=370,y=250)

e5=Entry(w,width=20)
e5.place(x=490,y=250)

b1=Button(w,text="Signup",width=10,fg="white",bg="black",command=log )
b1.place(x=390,y=340)


b2=Button(w,text="Cancel",width=10,fg="white",bg="black")
b2.place(x=500,y=340)

