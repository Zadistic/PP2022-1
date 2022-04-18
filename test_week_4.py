from audioop import mul
from sqlite3 import Row
from tkinter import*
import tkinter
from turtle import clear

expresion = ""

def ingresar(num):

	global expresion

	expresion = expresion + str(num)
	ecuacion.set(expresion)

#def dibujar1():

#	coord = 20, 10, 20, 50
#	line = C.create_line(coord)

#	coord = 10, 20, 20, 10
#	line = C.create_line(coord)

#def dibujar2():

#	coord = 40, 10, 60, 10
#	line = C.create_line(coord)

#	coord = 60, 10, 60, 30
#	line = C.create_line(coord)

#	coord = 60, 30, 40, 30
#	line = C.create_line(coord)

#	coord = 40, 30, 40, 50
#	line = C.create_line(coord)

#	coord = 40, 50, 60, 50
#	line = C.create_line(coord)

#def dibujar3():

#	coord = 80, 10, 100, 10
#	line = C.create_line(coord)

#	coord = 100, 10, 100, 30
#	line = C.create_line(coord)

#	coord = 100, 30, 80, 30
#	line = C.create_line(coord)

#	coord = 100, 30, 100, 50
#	line = C.create_line(coord)

#	coord = 80, 10, 100, 10
#	line = C.create_line(coord)

#	coord = 100, 50, 80, 50
#	line = C.create_line(coord)

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

	global expresion
	expresion = ""
	ecuacion.set("")

if __name__ == "__main__":

	interfaz = Tk()

	interfaz.configure(background="grey75")
	interfaz.title("Calculadora")
	interfaz.geometry("373x450")

	ecuacion = StringVar()

	C = Canvas(interfaz, bg="white", height=250, width=300)
	
	mostrar = Entry(interfaz, font=("arial", 14, "bold"), width=19, textvariable=ecuacion, bd=20, insertwidth=4,bg="white")
	mostrar.grid(columnspan=4, padx = 20, pady=50, ipadx=30, ipady=80, row= 0, column=0)

	case1 = Button(interfaz, text=" 1 ", fg="white", bg="grey39", command=lambda: ingresar(1), height=2, width=7)
	case1.grid(row=2, column=0)

	case2 = Button(interfaz, text=" 2 ", fg="white", bg="grey39", command=lambda: ingresar(2), height=2, width=7)
	case2.grid(row=2, column=1)

	case3 = Button(interfaz, text=" 3 ", fg="white", bg="grey39", command=lambda: ingresar(3), height=2, width=7)
	case3.grid(row=2, column=2)

	case4 = Button(interfaz, text=" 4 ", fg="white", bg="grey39", command=lambda: ingresar(4), height=2, width=7)
	case4.grid(row=3, column=0)

	case5 = Button(interfaz, text=" 5 ", fg="white", bg="grey39", command=lambda: ingresar(5), height=2, width=7)
	case5.grid(row=3, column=1)

	case6 = Button(interfaz, text=" 6 ", fg="white", bg="grey39", command=lambda: ingresar(6), height=2, width=7)
	case6.grid(row=3, column=2)

	case7 = Button(interfaz, text=" 7 ", fg="white", bg="grey39", command=lambda: ingresar(7), height=2, width=7)
	case7.grid(row=4, column=0)

	case8 = Button(interfaz, text=" 8 ", fg="white", bg="grey39", command=lambda: ingresar(8), height=2, width=7)
	case8.grid(row=4, column=1)

	case9 = Button(interfaz, text=" 9 ", fg="white", bg="grey39", command=lambda: ingresar(9), height=2, width=7)
	case9.grid(row=4, column=2)

	case0 = Button(interfaz, text=" 0 ", fg="white", bg="grey39", command=lambda: ingresar(0), height=2, width=7)
	case0.grid(row=5, column=0)

	suma = Button(interfaz, text=" + ", fg="white", bg="grey39", command=lambda: ingresar("+"), height=2, width=7)
	suma.grid(row=2, column=3)

	resta = Button(interfaz, text=" - ", fg="white", bg="grey39", command=lambda: ingresar("-"), height=2, width=7)
	resta.grid(row=3, column=3)

	multip = Button(interfaz, text=" * ", fg="white", bg="grey39", command=lambda: ingresar("*"), height=2, width=7)
	multip.grid(row=4, column=3)

	division = Button(interfaz, text=" / ", fg="white", bg="grey39", command=lambda: ingresar("/"), height=2, width=7)
	division.grid(row=5, column=3)

	resol = Button(interfaz, text=" = ", fg="white", bg="grey39", command=resolver, height=2, width=7)
	resol.grid(row=6, column=3)

	vaciar = Button(interfaz, text=" C ", fg="white", bg="maroon", command=limpiar, height=2, width=7)
	vaciar.grid(row=5, column="2")

	decimal= Button(interfaz, text=".", fg="white", bg="grey39", command=lambda: ingresar("."), height=2, width=7)
	decimal.grid(row=5, column=1)

	interfaz.mainloop()
