from audioop import mul
from sqlite3 import Row
from tkinter import*
import tkinter
from turtle import clear

expresion = ""

x=20
y1=10
y2=50
i=x
def dibujar(numeros):
  global x,y1,y2,i,x2

  if (numeros==1):

    coord = i+10,y1,i+10,y2
    mostrar.create_line(coord)
    mostrar.addtag_all
  i=i+30

def ingresar():

	global expresion

	#expresion = expresion + str(num)
	#ecuacion.set(expresion)

def resolver():

	try:

		global expresion

		resultado = str(eval(expresion))
		ecuacion.set(resultado)
		expresion = ""

	except:

		ecuacion.set(" error ")
		expresion = ""

def limpiar():

	mostrar.delete('all')
	
    
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

case2 = Button(interfaz, text=" 2 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case2.grid(row=2, column=1)

case3 = Button(interfaz, text=" 3 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case3.grid(row=2, column=2)

case4 = Button(interfaz, text=" 4 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case4.grid(row=3, column=0)

case5 = Button(interfaz, text=" 5 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case5.grid(row=3, column=1)

case6 = Button(interfaz, text=" 6 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case6.grid(row=3, column=2)

case7 = Button(interfaz, text=" 7 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case7.grid(row=4, column=0)

case8 = Button(interfaz, text=" 8 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case8.grid(row=4, column=1)

case9 = Button(interfaz, text=" 9 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case9.grid(row=4, column=2)

case0 = Button(interfaz, text=" 0 ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
case0.grid(row=5, column=0)

suma = Button(interfaz, text=" + ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
suma.grid(row=2, column=3)

resta = Button(interfaz, text=" - ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
resta.grid(row=3, column=3)

multip = Button(interfaz, text=" * ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
multip.grid(row=4, column=3)

division = Button(interfaz, text=" / ", fg="white", bg="grey39", command=lambda: dibujar(1), height=2, width=7)
division.grid(row=5, column=3)

resol = Button(interfaz, text=" = ", fg="white", bg="grey39", command=resolver, height=2, width=7)
resol.grid(row=6, column=3)

vaciar = Button(interfaz, text=" C ", fg="white", bg="maroon", command=limpiar, height=2, width=7)
vaciar.grid(row=5, column="2")
decimal= Button(interfaz, text=".", fg="white", bg="grey39", command=lambda: ingresar("."), height=2, width=7)
decimal.grid(row=5, column=1)

interfaz.mainloop()

