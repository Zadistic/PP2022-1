from audioop import mul
from sqlite3 import Row
from tkinter import*

def press(num): #función que acepta los números a través de teclado.

  global operador
  operador = operador + str(num)
  entradaTexto.set(operador)  #cambiar nombre variable
  
def resolver():

  try:

    global operador
    final = str(eval(operador))
    entradaTexto.set(final)
    salida = ""
  
  except:

    entradaTexto.set(" error ")
    salida = ""
  
def clear():

    global operador
    operador=("")
    entradaTexto.set("0")
  
interfaz = Tk()
interfaz.configure(bg="grey")
interfaz.title("CALCULEITOR")
interfaz.geometry("355x450")

entradaTexto = StringVar()

operador=""

salida = Entry(interfaz, font=("arial", 14, "bold"), width=19, textvariable=entradaTexto, bd=20, insertwidth=4,bg="white")
salida.grid(columnspan=4, padx = 10, pady=20, ipadx=40, ipady=50, row= 0, column=0)

ancho=7
largo=1

case7 = Button(interfaz, text = " 7 ", width = ancho, height = largo, command=lambda: press(7))
case7.grid(row=2, column=0)

case8 = Button(interfaz, text = " 8 ", width = ancho, height = largo, command=lambda: press(8))
case8.grid(row=2, column=1)

case9 = Button(interfaz, text=" 9 ", width=ancho, height=largo, command=lambda: press(9))
case9.grid(row=2, column=2)

case4 = Button(interfaz, text=" 4 ", width=ancho, height=largo, command=lambda: press(4))
case4.grid(row=3, column=0)

case5 = Button(interfaz, text=" 5 ", width=ancho, height=largo, command=lambda: press(5))
case5.grid(row=3, column=1)

case6 = Button(interfaz, text=" 6 ", width=ancho, height=largo, command=lambda: press(6))
case6.grid(row=3, column=2)

case1 = Button(interfaz, text=" 1 ", width=ancho, height=largo, command=lambda: press(1))
case1.grid(row=4, column=0)

case2 = Button(interfaz, text=" 2 ", width=ancho, height=largo, command=lambda: press(2))
case2.grid(row=4, column=1)

case3 = Button(interfaz, text=" 3 ", width=ancho, height=largo, command=lambda: press(3))
case3.grid(row=4, column=2)

case0 = Button(interfaz, text=" 0 ", width=ancho, height=largo, command=lambda: press(0))
case0.grid(row=5, column=1)

suma = Button(interfaz, font=("arial",9,"bold"),text=" + ", width=ancho, height=largo, command=lambda: press("+"))
suma.grid(row=5, column=2)

resta = Button(interfaz, font=("arial",9,"bold"),text=" — ", width=ancho, height=largo, command=lambda: press("-"))
resta.grid(row=5, column=0)

multip = Button(interfaz, font=("arial",9,"bold"),text=" x ", width=ancho, height=largo, command=lambda: press("x"))
multip.grid(row=6, column=0)

division = Button(interfaz, font=("arial",9,"bold"),text=" / ", width=ancho, height=largo, command=lambda: press("/"))
division.grid(row=6, column=1)

borrar = Button(interfaz, font=("arial",9,"bold"),text=" C ", width=ancho, height=largo, command=clear)
borrar.grid(row=6, column=2)

resol = Button(interfaz, text=" RESOLVER ", width=28, height=2, command=resolver, pady=10)
resol.grid(row=7, column=1)

clear()

interfaz.mainloop()