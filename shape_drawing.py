from tkinter import *
import turtle


def işlemler(x):
    s1=float(giriş.get())
    
    if x==0:
        s1=s1*20
        pen=turtle.Turtle()
        pen.pencolor("red")
        pen.pensize(8),
        pen.speed(5)
        for i in range(3):
            pen.forward(s1)
            pen.left(120)
        turtle.done()
    
    if x==1:
        s1=s1*20
        pen=turtle.Turtle()
        pen.pencolor("green")
        pen.pensize(8)
        pen.speed(5)
        for i in range(4):
            pen.forward(s1)
            pen.right(90)
        turtle.done()
    
    if x==2:
        s1=s1*20
        pen=turtle.Turtle()
        pen.pencolor("blue")
        pen.pensize(8)
        pen.speed(5)
        pen.circle(s1)
        turtle.done()
        
    if x==3:
        s1=s1*20
        pen=turtle.Turtle()
        pen.pencolor("purple")
        pen.pensize(8)
        pen.speed(5)
        for i in range(5):
            pen.forward(s1)
            pen.left(72)
        turtle.done()
    
    if x==4:
        s1=s1*20
        pen=turtle.Turtle()
        pen.pencolor("yellow")
        pen.pensize(8)
        pen.speed(5)
        for i in range(6):
            pen.forward(s1)
            pen.left(60)
        turtle.done()
        
    if x==5:
        s1=s1*20
        pen=turtle.Turtle()
        pen.pencolor("orange")
        pen.pensize(8)
        pen.speed(5)
        for i in range(8):
            pen.forward(s1)
            pen.left(45)
        turtle.done()
            

pencere=Tk()
pencere.geometry("360x200")
pencere.title("GEO-ÇİZ")

giriş = Entry(font="arial 15 bold",fg="dark blue",width=28)
giriş.place(x=20,y=130)

label=Label(pencere,font="arial 8 bold",fg="white",bg="grey",text="Birim uzunluğunu giriniz ve çizmek isteğiniz şekile basınız.")
label.pack()
label.place(x=13,y=170)


butonlar = []

for i in range(6):
    butonlar.append(Button(font="arial 15 bold",bg="grey",fg="dark blue",width=7,command=lambda x=i:işlemler(x)))
 
index=0

butonlar[0]['text']="Üçgen"
butonlar[1]['text']="Kare"
butonlar[2]['text']="Daire"
butonlar[3]['text']="Beşgen"
butonlar[4]['text']="Altıgen"
butonlar[5]['text']="Sekizgen"

for i in range(0,2):
    for j in range(0,3):
        butonlar[index].place(x=20+110*j,y=20+i*50)
        index+=1


pencere.mainloop()