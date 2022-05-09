from sqlite3 import Row, connect
from tkinter import*
import tkinter
from tkinter import ttk
import tkinter.font as tkFont

x=20
y1=10
y2=50
i=x
contadori=x
contadorf=x
op_color = "#0ba37b"
num_color = "#ff0090"

def fraccion():

   global i, y1, y2, contadori, contadorf

   coord = contadori, y1+45, contadorf, y2+5
   dibujo.create_line(coord, fill=op_color)
   dibujo.addtag_all

   y1 = 65
   y2 = 105

   i = contadori
   contadorf = i

def dibujar(numeros):
   
    global flag, y1, y2, i, contadori, contadorf
    if (numeros == 0): #Nro 0
    
        coord =i, y1, i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+40, i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+40, i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1,i , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1, i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all

    if (numeros == 1): #Nro 1

        coord = i+10, y1, i+10, y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 2): #Nro 2
        
        coord = i, y1, i+20, y2-40
        dibujo.create_line(coord, fill=num_color)
        coord = i+20, y1, i+20, y2-20
        dibujo.create_line(coord, fill=num_color)
        coord = i+20, y1+20, i, y2-20
        dibujo.create_line(coord, fill=num_color)
        coord = i, y1+20, i, y2
        dibujo.create_line(coord, fill=num_color)
        coord = i, y1+40, i+20, y2

        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 3): #Nro 3

        coord = i, y1, i+20, y2-40
        dibujo.create_line(coord, fill=num_color)
        coord = i+20, y1, i+20, y2-20
        dibujo.create_line(coord, fill=num_color)
        coord = i+20, y1+20, i, y2-20
        dibujo.create_line(coord, fill=num_color)
        coord = i+20, y1+20, i+20, y2
        dibujo.create_line(coord, fill=num_color)
        coord = i, y1, i+20, y2-40
        dibujo.create_line(coord, fill=num_color)
        coord = i+20, y1+40, i, y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 4): #Nro 4

        coord =i, y1+20,i , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1+20,i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 5): #Nro 5

        coord =i, y1,i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1,i , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1+20,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1+40,i , y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 6): #Nro 6

        coord =i, y1 ,i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1 ,i , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+40 ,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1+40,i+20 , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20, y2-20
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 7): #Nro 7

        coord =i, y1,i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 8): #Nro 8

        coord =i, y1,i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+40,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1,i , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        dibujo.addtag_all
        
    if (numeros == 9): #Nro 9

        coord =i, y1,i , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        dibujo.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        dibujo.create_line(coord, fill=num_color)
        coord =i, y1,i+20 , y2-40
        dibujo.create_line(coord, fill=num_color)
        
    if (numeros == 10): #Suma
        
        y1 = 10
        y2 = 50

        coord =i+10, y1, i+10 , y2-10
        dibujo.create_line(coord, fill=op_color)
        coord =i, y1+15, i+20 , y2-25
        dibujo.create_line(coord, fill=op_color)
        dibujo.addtag_all
        contadori=i+30

    if (numeros == 11): #Resta

        y1 = 10
        y2 = 50

        coord =i, y1+20,i+20 , y2-20
        dibujo.create_line(coord, fill=op_color)
        dibujo.addtag_all
        contadori=i+30
        
    if (numeros == 12): #Multiplicacion
        
        y1 = 10
        y2 = 50
        
        coord =i, y1+10, i+10, y2-15
        dibujo.create_line(coord, fill=op_color)
        coord =i+10, y1+10, i, y2-15
        dibujo.create_line(coord, fill=op_color)
        dibujo.addtag_all
        contadori=i+30

    if (numeros == 13): #Potencia

        return 0

    if (numeros == 14): #Factorial
        #recta vertical
        coord =i+3, y1,i+3 , y2-10
        dibujo.create_line(coord, fill=op_color)
        #punto
        coord=i,y1+40,i+5,y2-5
        dibujo.create_oval(coord,fill=op_color)
        
        
        dibujo.addtag_all
        
    if (numeros == 15): #Seno 

        #S
        coord =i, y1,i+20 , y2-40
        dibujo.create_line(coord, fill=op_color)
        coord =i, y1,i, y2-20
        dibujo.create_line(coord, fill=op_color)
        coord =i, y1+20,i+20, y2-20
        dibujo.create_line(coord, fill=op_color)
        coord =i+20, y1+20,i+20, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+20, y1+40,i, y2
        dibujo.create_line(coord, fill=op_color)
        #E
        coord =i+25, y1,i+45, y2-40
        dibujo.create_line(coord, fill=op_color)
        coord =i+25, y1,i+25, y2-20
        dibujo.create_line(coord, fill=op_color)
        coord =i+25, y1+20,i+45, y2-20
        dibujo.create_line(coord, fill=op_color)
        coord =i+25, y1+20,i+25, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+25, y1+40,i+45, y2
        dibujo.create_line(coord, fill=op_color)
        #N
        coord =i+50, y1,i+50, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+50, y1,i+75, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+75, y1,i+75, y2
        dibujo.create_line(coord, fill=op_color)

    
        dibujo.addtag_all
        i=i+60
    
    if (numeros == 16): #Coseno

        #C
        coord =i, y1,i+20 , y2-40
        dibujo.create_line(coord, fill=op_color)
        coord=i,y1,i,y2
        dibujo.create_line(coord,fill=op_color)
        coord =i, y1+40,i+20 , y2
        dibujo.create_line(coord, fill=op_color)
        #O
        coord =i+25, y1, i+45 , y2-40
        dibujo.create_line(coord, fill=op_color)
        coord =i+25, y1+40, i+45 , y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+25, y1,i+25 , y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+45, y1, i+45 , y2
        dibujo.create_line(coord, fill=op_color)
        #S
        coord =i+50, y1,i+70 , y2-40
        dibujo.create_line(coord, fill=op_color)
        coord =i+50, y1,i+50, y2-20
        dibujo.create_line(coord, fill=op_color)
        coord =i+50, y1+20,i+70, y2-20
        dibujo.create_line(coord, fill=op_color)
        coord =i+70, y1+20,i+70, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+70, y1+40,i+50, y2
        dibujo.create_line(coord, fill=op_color)
        dibujo.addtag_all
        i=i+60
        

    if (numeros == 17): #Tangente

        #T
        coord =i+15, y1,i+15 , y2
        dibujo.create_line(coord, fill=op_color)
        coord =i, y1,i+30 , y2-40
        dibujo.create_line(coord, fill=op_color)
        #A
        coord =i+30, y1+40,i+40 , y2-40
        dibujo.create_line(coord, fill=op_color)
        coord =i+40, y1,i+50 , y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+35, y1+20,i+45 , y2-20
        dibujo.create_line(coord, fill=op_color)
        #N
        coord =i+52, y1,i+52, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+52, y1,i+77, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+77, y1,i+77, y2
        dibujo.create_line(coord, fill=op_color)

        dibujo.addtag_all
        i=i+60

    if (numeros == 18): #Abre Parentesis

        return 0

    if (numeros == 19): #Cierre parentesis

        return 0

    if(numeros == 20):#raiz
        coord =i, y1+20,i+10, y2
        dibujo.create_line(coord, fill=op_color)
        coord =i+10, y1+40,i+15, y2-45
        dibujo.create_line(coord, fill=op_color)
        coord =i+15, y1-5,i+25, y2-45
        dibujo.create_line(coord, fill=op_color)

        dibujo.addtag_all
        

    i=i+30
    contadorf=contadorf+30
  
def limpiar():

   global i, y1, y2, contadori, contadorf

   dibujo.delete("all")
   
   i=x
   contadorf=x
   contadori=x
   y1 = 10
   y2 = 50
	 
interfaz = Tk()
interfaz.configure(background="grey70")
interfaz.title("CALCULADORA")
interfaz.geometry("1920x1080")

text_square = ttk.Entry(width=100)
text_square.place(x=20, y= 400, height=50)

dibujo = Canvas(interfaz)
dibujo.grid(columnspan=5, pady=20, ipadx=300, ipady=30, row= 0, column=0)

altura = 1
ancho = 8
fontStyle = tkFont.Font(family="Lucida Grande", size=22)

color_selection = Button(interfaz, text=" COLOR ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(1), height=altura, width=ancho)
color_selection.grid(row=0, column=5)

coord_button = Button(interfaz, text=" COORD ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(1), height=altura, width=ancho)
coord_button.grid(row=0, column=6)

#Botón para número 1
case1 = Button(interfaz, text=" 1 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(1), height=altura, width=ancho)
case1.grid(row=5, column=1)

#Botón para número 2
case2 = Button(interfaz, text=" 2 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(2), height=altura, width=ancho)
case2.grid(row=5, column=2)

#Botón para número 3
case3 = Button(interfaz, text=" 3 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(3), height=altura, width=ancho)
case3.grid(row=5, column=3)

#Botón para número 4
case4 = Button(interfaz, text=" 4 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(4), height=altura, width=ancho)
case4.grid(row=4, column=1)

#Botón para número 5
case5 = Button(interfaz, text=" 5 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(5), height=altura, width=ancho)
case5.grid(row=4, column=2)

#Botón para número 6
case6 = Button(interfaz, text=" 6 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(6), height=altura, width=ancho)
case6.grid(row=4, column=3)

#Botón para número 7
case7 = Button(interfaz, text=" 7 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(7), height=altura, width=ancho)
case7.grid(row=3, column=1)

#Botón para número 8
case8 = Button(interfaz, text=" 8 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(8), height=altura, width=ancho)
case8.grid(row=3, column=2)

#Botón para número 9
case9 = Button(interfaz, text=" 9 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(9), height=altura, width=ancho)
case9.grid(row=3, column=3)

#Botón para número 0
case0 = Button(interfaz, text=" 0 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(0), height=altura, width=ancho)
case0.grid(row=6, column=1)

#Botón para operador +
suma = Button(interfaz, text=" + ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(10), height=altura, width=ancho)
suma.grid(row=3, column=4)

#Botón para operador -
resta = Button(interfaz, text=" — ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(11), height=altura, width=ancho)
resta.grid(row=4, column=4)

#Botón para operador X
multip = Button(interfaz, text=" X ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(12), height=altura, width=ancho)
multip.grid(row=5, column=4)

#Botón para operador /
division = Button(interfaz, text=" / ", font= fontStyle, fg="white", bg="grey39",
command=lambda: fraccion(), height=altura, width=ancho)
division.grid(row=6, column=4)

#Botón para operador =
resol = Button(interfaz, text=" = ", font= fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
resol.grid(row=6, column=3)

#Botón para VACIAR
vaciar = Button(interfaz, text=" AC ",relief=FLAT, font= fontStyle, fg="white", bg="#611115",
command=limpiar, height=altura, width=ancho)
vaciar.grid(row=2, column=4)

#Botón para operador seno
seno = Button(interfaz, text=" sen ", font = fontStyle, fg= "white", bg="grey39",command=lambda:dibujar(15),
height=altura, width=ancho)
seno.grid(row=3, column=0)

#Botón para operador coseno
coseno = Button(interfaz, text=" cos ", font = fontStyle, fg= "white", bg="grey39",command=lambda:dibujar(16),
height=altura, width=ancho)
coseno.grid(row=4, column=0)

#Botón para operador potencia
potencia = Button(interfaz, text=" x² ", font = fontStyle, fg= "white", bg="grey39",
height=altura, width=ancho)
potencia.grid(row=6, column=0)

#Botón para operador raiz
raiz = Button(interfaz, text="√", font = fontStyle, fg= "white", bg="grey39",command=lambda:dibujar(20),
height=altura, width=ancho)
raiz.grid(row=2, column=2)

#Botón para operador tangente
tang = Button(interfaz, text=" tan ", font = fontStyle, fg= "white", bg="grey39",command=lambda:dibujar(17),
height=altura, width=ancho)
tang.grid(row=5, column=0)

#Botón para operador factorial
fact = Button(interfaz, text=" x! ", font = fontStyle, fg= "white", bg="grey39",command=lambda:dibujar(14),
height=altura, width=ancho)
fact.grid(row=2, column=0)

#Botón para operador decimal
decimal = Button(interfaz, text=" . ", font = fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
decimal.grid(row = 6, column=2)

#Botón para Abre Paréntesis
abreP = Button(interfaz, text=" ( ", font = fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
abreP.grid(row = 2, column= 1)

#Botón para Cierre Paréntesis
cierreP = Button(interfaz, text=" ) ", font = fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
cierreP.grid(row = 2, column= 3)

interfaz.mainloop()