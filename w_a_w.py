from audioop import mul
from sqlite3 import Row
from tkinter import*
import tkinter
from turtle import clear, color

expresion = ""

x=20
y1=10
y2=50
flag = 0

denom = 65

i=x
contadori=x
contadorf=x

op_color = "#f56464"
num_color = "violet red"

def fraccion():

   global flag, y1, y2, contadori,contadorf

   coord = contadori, y1+45, contadorf, y2+5
   mostrar.create_line(coord, fill=op_color)
   mostrar.addtag_all

   y1 = 65
   y2 = 105

   flag = 1

def dibujar(numeros):

  global flag, x,y1,y2,i,contadori,contadorf

  if (numeros == 0): #Nro 0
   
      coord =i, y1,i+20 , y2-40
      mostrar.create_line(coord, fill=num_color)
      coord =i, y1+40,i+20 , y2
      mostrar.create_line(coord, fill=num_color)
      coord =i, y1+40,i+20 , y2-40
      mostrar.create_line(coord, fill=num_color)
      coord =i, y1,i , y2
      mostrar.create_line(coord, fill=num_color)
      coord =i+20, y1,i+20 , y2
      mostrar.create_line(coord, fill=num_color)
      mostrar.addtag_all

  if (numeros == 1): #Nro 1

      coord = i+10,y1,i+10,y2
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
      
      coord =i+10, y1,i+10 , y2-10
      mostrar.create_line(coord, fill=op_color)
      coord =i, y1+15,i+20 , y2-25
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

  
  i=i+30
  contadorf=contadorf+30
  
def ingresar():
   return 0

def resolver():
   return 0

def limpiar():

   global i, y1, y2, contadori, contadorf

   mostrar.delete("all")
   i=x
   contadorf=x
   contadori=x
   y1 = 10
   y2 = 50
	 
interfaz = Tk()
interfaz.configure(background="grey75")
interfaz.title("Calculadora")
interfaz.geometry("480x700")
ecuacion = StringVar()

mostrar = Canvas(interfaz)
mostrar.place(x=50,y=50,height=250, width=300)
mostrar.grid(columnspan=4, padx = 20, pady=25, ipadx=30, ipady=80, row= 0, column=0)

case1 = Button(interfaz, text=" 1 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case1.grid(row=2, column=0)

case2 = Button(interfaz, text=" 2 ", fg="white", bg="grey39", command=lambda: dibujar(2), height=2, width=7)
case2.grid(row=2, column=1)

case3 = Button(interfaz, text=" 3 ", fg="white", bg="grey39", command=lambda: dibujar(3), height=2, width=7)
case3.grid(row=2, column=2)

case4 = Button(interfaz, text=" 4 ", fg="white", bg="grey39", command=lambda: dibujar(4), height=2, width=7)
case4.grid(row=3, column=0)

case5 = Button(interfaz, text=" 5 ", fg="white", bg="grey39", command=lambda: dibujar(5), height=2, width=7)
case5.grid(row=3, column=1)

case6 = Button(interfaz, text=" 6 ", fg="white", bg="grey39", command=lambda: dibujar(6), height=2, width=7)
case6.grid(row=3, column=2)

case7 = Button(interfaz, text=" 7 ", fg="white", bg="grey39", command=lambda: dibujar(7), height=2, width=7)
case7.grid(row=4, column=0)

case8 = Button(interfaz, text=" 8 ", fg="white", bg="grey39", command=lambda: dibujar(8), height=2, width=7)
case8.grid(row=4, column=1)

case9 = Button(interfaz, text=" 9 ", fg="white", bg="grey39", command=lambda: dibujar(9), height=2, width=7)
case9.grid(row=4, column=2)

case0 = Button(interfaz, text=" 0 ", fg="white", bg="grey39", command=lambda: dibujar(0), height=2, width=7)
case0.grid(row=5, column=0)

suma = Button(interfaz, text=" + ", fg="white", bg="grey39", command=lambda: dibujar(10), height=2, width=7)
suma.grid(row=2, column=3)

resta = Button(interfaz, text=" - ", fg="white", bg="grey39", command=lambda: dibujar(11), height=2, width=7)
resta.grid(row=3, column=3)

multip = Button(interfaz, text=" * ", fg="white", bg="grey39", command=lambda: dibujar(12), height=2, width=7)
multip.grid(row=4, column=3)

division = Button(interfaz, text=" / ", fg="white", bg="grey39", command=lambda: fraccion(), height=2, width=7)
division.grid(row=5, column=3)

resol = Button(interfaz, text=" = ", fg="white", bg="grey39",  height=2, width=7)
resol.grid(row=6, column=3)

vaciar = Button(interfaz, text=" AC ", fg="white", bg="maroon", command=limpiar, height=2, width=7)
vaciar.grid(row=5, column="2")
decimal= Button(interfaz, text=".", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
decimal.grid(row=5, column=1)

interfaz.mainloop()
