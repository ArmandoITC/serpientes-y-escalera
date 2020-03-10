from tkinter import *
import time
import random
global x,y,Pos,j,imagen,Ju,turno,color,Casilla
Ju=0
x=[0]
y=[525]
Casilla=[0]
j=""
turno=0
Dado=0
color=["white","blue","red"]
def ganador ():#verifica si hay ganador 
    l=Label(ventana,text=" \t\t\t\t  \t\t\t\t ",bg="black").place(x=700,y=75)
    l=Label(ventana,text=(" has ganado jugador :  "+str(turno+1)),bg="blue").place(x=700,y=75)
    B1.config(state="disable")
    B2.config(state="disable")
    


    
def fichas ():#crea las fichas
    global x,y,Pos,j,imagen,Ju
    i=0
    L=j.get()
    Ju=int(L)
    while (i <(Ju)):
        
        x.append(0)
        y.append(525)
        Casilla.append(0)
        i=i+1
    fondo(imagen)

def comp(): #reinicia los turnos
    global turno,Ju
    if(turno==Ju):
        turno=0
        


def Turno ():#aumenta los turnos
    global turno,Ju
    l=Label(ventana,text=" \t\t\t\t  \t\t\t\t ",bg="black").place(x=600,y=75)
    if(turno<Ju):
        turno=turno+1
    comp()
    

def dado (): #tira el dado
    global turno,Casilla,Dado
    Dado=random.randint(1,6)
    l=Label(ventana,text=Dado).grid(column=0,row=0)
    Casilla[turno]=Casilla[turno]+Dado
    l=Label(ventana,text=Casilla[turno]).grid(column=14,row=13)
    if(64<Casilla[turno]):
        Casilla[turno]=64-(Casilla[turno]-64)
    if(64==Casilla[turno]):
        ganador()

    
    escalera()
    

def escalera(): # verifica si hay escalera
    global Casilla,turno
    if(Casilla[turno]==1):
        l=Label(ventana,text=("Felicidades tu tiro cayo en 1 pasas a 19 jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=19
    if(Casilla[turno]==4):
        l=Label(ventana,text=("  Felicidades tu tiro cayo en 4 pasas a 11 jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=11
    if(Casilla[turno]==7):
        l=Label(ventana,text=("  Felicidades tu tiro cayo en 7 pasas a 25 jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=25
    if(Casilla[turno]==17):
        l=Label(ventana,text=("  Felicidades tu tiro cayo en 17 pasas a 31 jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=31
    if(Casilla[turno]==22):
        l=Label(ventana,text=("  Felicidades tu tiro cayo en 22 pasas a 50 jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=50
    if(Casilla[turno]==42):
        l=Label(ventana,text=("  Felicidades tu tiro cayo en 42 pasas a 54 jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=54
    serpiente()



def serpiente():#verifica si hay serpiente
    global Casilla,turno,imagen
    if(Casilla[turno]==13):
        l=Label(ventana,text=("   tu tiro cayo en 13 pasas a 5 :(  jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=5
    if(Casilla[turno]==38):
        l=Label(ventana,text=("   tu tiro cayo en 38 pasas a 9  :(  jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=9
    if(Casilla[turno]==47):
        l=Label(ventana,text=("   tu tiro cayo en 47 pasas a 14  :(  jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=14
    if(Casilla[turno]==53):
        l=Label(ventana,text=("   tu tiro cayo en 53 pasas a 20  :(  jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=20
    if(Casilla[turno]==57):
        l=Label(ventana,text=("   tu tiro cayo en 57 pasas a 23  :(  jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=23
    if(Casilla[turno]==62):
        l=Label(ventana,text=("   tu tiro cayo en 62 pasas a 34   :(   jugador: "+str(turno+1)),bg="blue").place(x=600,y=75)
        Casilla[turno]=34
    fondo(imagen)


    
    
def fondo (img): #limpia el tablero
    global Dado
    l=Label(ventana,image=img).place(x=0, y=0)
    l=Label(ventana,text=Dado).place(x=0, y=575)
    jugadores()



def jugadores (): # dibuja las posiciones 
    global x,y,Pos,Ju,color,S,Casilla
    S=0
    i=0
    while(i<Ju):
        g=0
        if(Casilla[i]==0): #1
            y[i]=700
            x[i]=(g*75)

            
        if(1<=Casilla[i]<9): #1
            y[i]=525
            g=Casilla[i]-1
            x[i]=(g*75)


        
        if(8<Casilla[i]<17): #1
            y[i]=450
            g=Casilla[i]-8
            x[i]=600-(g*75)

        if(16<Casilla[i]<25):#2
            y[i]=375
            g=Casilla[i]-17
            x[i]=(g*75)

        if(24<Casilla[i]<33):#1
            y[i]=300
            g=Casilla[i]-24
            x[i]=600-(g*75)
        
        if(32<Casilla[i]<41):#2
            y[i]=225
            g=Casilla[i]-33
            x[i]=(g*75)
            
        if(40<Casilla[i]<49):#1
            y[i]=150
            g=Casilla[i]-40
            x[i]=600-(g*75)
            
        if(48<Casilla[i]<57):#2
            y[i]=75
            g=Casilla[i]-49
            x[i]=(g*75)

        if(56<Casilla[i]<=64):#1
            y[i]=0
            g=Casilla[i]-56
            x[i]=600-(g*75)

        if(S==3):
            S=0
        l=Label(ventana,text=Casilla[i]).grid(column=13+i,row=13+i)

        
        c=Canvas(ventana,width=75,height=75,bg="black")
        c.place(x=x[i],y=y[i])
        c.create_oval(5,5,70,70,fill=color[S])
        i=i+1
        S=S+1

ventana=Tk()
ventana.config(bg="black")
ventana.geometry("875x600")
j=StringVar()
l=Label(ventana,text="numero de jugadores ").grid(column=13,row=13)
cuadro00=Entry(ventana,textvariable=j,state="normal",width=2)
cuadro00.grid(column=1,row=1)
B=Button(ventana,text="ok",command=fichas).grid(column=10,row=1)
imagen=PhotoImage(file="serpientes.gif")
B2=Button(ventana,text="dado",command=dado,bg="blue")
B2.place(x=602,y=0)
B1=Button(ventana,text="turno",command=Turno,bg="blue")
B1.place(x=602,y=30)


ventana.mainloop
