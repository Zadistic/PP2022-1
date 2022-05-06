from sqlite3 import Row, connect
from tkinter import*
import tkinter
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
   mostrar.create_line(coord, fill=op_color)
   mostrar.addtag_all

   y1 = 65
   y2 = 105

   i = contadori
   contadorf = i

def dibujar(numeros):
   
    global flag, y1, y2, i, contadori, contadorf
    if (numeros == 0): #Nro 0
    
        coord =i, y1, i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+40, i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+40, i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1,i , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1, i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all

    if (numeros == 1): #Nro 1

        coord = i+10, y1, i+10, y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 2): #Nro 2
        
        coord = i, y1, i+20, y2-40
        mostrar.create_line(coord, fill=num_color)
        coord = i+20, y1, i+20, y2-20
        mostrar.create_line(coord, fill=num_color)
        coord = i+20, y1+20, i, y2-20
        mostrar.create_line(coord, fill=num_color)
        coord = i, y1+20, i, y2
        mostrar.create_line(coord, fill=num_color)
        coord = i, y1+40, i+20, y2

        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 3): #Nro 3

        coord = i, y1, i+20, y2-40
        mostrar.create_line(coord, fill=num_color)
        coord = i+20, y1, i+20, y2-20
        mostrar.create_line(coord, fill=num_color)
        coord = i+20, y1+20, i, y2-20
        mostrar.create_line(coord, fill=num_color)
        coord = i+20, y1+20, i+20, y2
        mostrar.create_line(coord, fill=num_color)
        coord = i, y1, i+20, y2-40
        mostrar.create_line(coord, fill=num_color)
        coord = i+20, y1+40, i, y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 4): #Nro 4

        coord =i, y1+20,i , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1+20,i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 5): #Nro 5

        coord =i, y1,i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1,i , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1+20,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1+40,i , y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 6): #Nro 6

        coord =i, y1 ,i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1 ,i , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+40 ,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1+40,i+20 , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20, y2-20
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 7): #Nro 7

        coord =i, y1,i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 8): #Nro 8

        coord =i, y1,i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+40,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1,i , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        mostrar.addtag_all
        
    if (numeros == 9): #Nro 9

        coord =i, y1,i , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1+20,i+20 , y2-20
        mostrar.create_line(coord, fill=num_color)
        coord =i+20, y1,i+20 , y2
        mostrar.create_line(coord, fill=num_color)
        coord =i, y1,i+20 , y2-40
        mostrar.create_line(coord, fill=num_color)
        
    if (numeros == 10): #Suma
        
        y1 = 10
        y2 = 50

        coord =i+10, y1, i+10 , y2-10
        mostrar.create_line(coord, fill=op_color)
        coord =i, y1+15, i+20 , y2-25
        mostrar.create_line(coord, fill=op_color)
        mostrar.addtag_all
        contadori=i+30

    if (numeros == 11): #Resta

        y1 = 10
        y2 = 50

        coord =i, y1+20,i+20 , y2-20
        mostrar.create_line(coord, fill=op_color)
        mostrar.addtag_all
        contadori=i+30
        
    if (numeros == 12): #Multiplicacion
        
        y1 = 10
        y2 = 50
        
        coord =i, y1+10, i+10, y2-15
        mostrar.create_line(coord, fill=op_color)
        coord =i+10, y1+10, i, y2-15
        mostrar.create_line(coord, fill=op_color)
        mostrar.addtag_all
        contadori=i+30

    if (numeros == 13): #Potencia

        return 0

    if (numeros == 14): #Factorial

        return 0

    if (numeros == 15): #Seno

        return 0

    if (numeros == 16): #Coseno

        return 0

    if (numeros == 17): #Tangente

        return 0


    if (numeros == 13): #Abre Parentesis

        return 0


    if (numeros == 13): #Cierre parentesis



        return 0


    i=i+30
    contadorf=contadorf+30
  
def limpiar():

   global i, y1, y2, contadori, contadorf

   mostrar.delete("all")
   
   i=x
   contadorf=x
   contadori=x
   y1 = 10
   y2 = 50
	 
interfaz = Tk()
interfaz.configure(background="grey70")
interfaz.title("Calculadora")
interfaz.geometry("1920x1080")

mostrar = Canvas(interfaz)
mostrar.grid(columnspan=4, pady=20, ipadx=132, ipady=50, row= 0, column=0)

altura = 1
ancho = 8
fontStyle = tkFont.Font(family="Lucida Grande", size=22)

case1 = Button(interfaz, text=" 1 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(1), height=altura, width=ancho)
case1.grid(row=4, column=1)

case2 = Button(interfaz, text=" 2 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(2), height=altura, width=ancho)
case2.grid(row=4, column=2)

case3 = Button(interfaz, text=" 3 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(3), height=altura, width=ancho)
case3.grid(row=4, column=3)

case4 = Button(interfaz, text=" 4 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(4), height=altura, width=ancho)
case4.grid(row=3, column=1)

case5 = Button(interfaz, text=" 5 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(5), height=altura, width=ancho)
case5.grid(row=3, column=2)

case6 = Button(interfaz, text=" 6 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(6), height=altura, width=ancho)
case6.grid(row=3, column=3)

case7 = Button(interfaz, text=" 7 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(7), height=altura, width=ancho)
case7.grid(row=2, column=1)

case8 = Button(interfaz, text=" 8 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(8), height=altura, width=ancho)
case8.grid(row=2, column=2)

case9 = Button(interfaz, text=" 9 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(9), height=altura, width=ancho)
case9.grid(row=2, column=3)

case0 = Button(interfaz, text=" 0 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(0), height=altura, width=ancho)
case0.grid(row=5, column=1)

suma = Button(interfaz, text=" + ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(10), height=altura, width=ancho)
suma.grid(row=2, column=4)

resta = Button(interfaz, text=" - ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(11), height=altura, width=ancho)
resta.grid(row=3, column=4)

multip = Button(interfaz, text=" * ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(12), height=altura, width=ancho)
multip.grid(row=4, column=4)

division = Button(interfaz, text=" / ", font= fontStyle, fg="white", bg="grey39",
command=lambda: fraccion(), height=altura, width=ancho)
division.grid(row=5, column=4)

resol = Button(interfaz, text=" = ", font= fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
resol.grid(row=5, column=3)

vaciar = Button(interfaz, text=" AC ",relief=FLAT, font= fontStyle, fg="white", bg="#611115",
command=limpiar, height=altura, width=ancho)
vaciar.grid(row=6, column=0)

seno = Button(interfaz, text=" sin ", font = fontStyle, fg= "white", bg="grey39",
height=altura, width=ancho)
seno.grid(row=3, column=0)

coseno = Button(interfaz, text=" cos ", font = fontStyle, fg= "white", bg="grey39",
height=altura, width=ancho)
coseno.grid(row=4, column=0)

potencia = Button(interfaz, text=" x² ", font = fontStyle, fg= "white", bg="grey39",
height=altura, width=ancho)
potencia.grid(row=6, column=2)

tang = Button(interfaz, text=" tan ", font = fontStyle, fg= "white", bg="grey39",
height=altura, width=ancho)
tang.grid(row=5, column=0)

fact = Button(interfaz, text=" x! ", font = fontStyle, fg= "white", bg="grey39",
height=altura, width=ancho)
fact.grid(row=2, column=0)

decimal = Button(interfaz, text=" . ", font = fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
decimal.grid(row = 5, column=2)

interfaz.mainloop()