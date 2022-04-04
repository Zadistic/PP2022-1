from tkinter import*

def press(num): #momento en el que se presionan los numeros
  global operador 
  operador=operador+str(num)
  entradaTexto.set(operador)
  
def resolver():
  print("En proceso.")
  
 # global operador
  #try:
   #   opera=str(eval(operador))
    #  entradaTexto.set(opera)
  #except:
   #   entradaTexto.set("ERROR")
  #operador = ""
  
def clear():
    global operador
    operador=("")
    entradaTexto.set("0")
  
ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("280x450")
ventana.configure(bg="grey")
entradaTexto=StringVar()
operador=""

Salida=Entry(ventana,font=("arial", 14,"bold"),width=19,textvariable=entradaTexto,bd=20,insertwidth=4,bg="powder blue").place(x=15,y=10)

ancho=8
largo=3

Button(ventana, text="7", width=ancho, height=largo, command=lambda: press(7)).place(x=35,y=80)
Button(ventana, text="8", width=ancho, height=largo, command=lambda: press(8)).place(x=105,y=80)
Button(ventana, text="9", width=ancho, height=largo, command=lambda: press(9)).place(x=175,y=80)
Button(ventana, text="4", width=ancho, height=largo, command=lambda: press(4)).place(x=35,y=140)
Button(ventana, text="5", width=ancho, height=largo, command=lambda: press(5)).place(x=105,y=140)
Button(ventana, text="6", width=ancho, height=largo, command=lambda: press(6)).place(x=175,y=140)
Button(ventana, text="1", width=ancho, height=largo, command=lambda: press(1)).place(x=35,y=200)
Button(ventana, text="2", width=ancho, height=largo, command=lambda: press(2)).place(x=105,y=200)
Button(ventana, text="3", width=ancho, height=largo, command=lambda: press(3)).place(x=175,y=200)
Button(ventana, text="0", width=ancho, height=largo, command=lambda: press(0)).place(x=35,y=260)
Button(ventana, font=("arial",9,"bold"),text="+", width=ancho, height=largo, command=lambda: press("+")).place(x=105,y=260)
Button(ventana, font=("arial",9,"bold"),text="—", width=ancho, height=largo, command=lambda: press("-")).place(x=175,y=260)
Button(ventana, font=("arial",9,"bold"),text="x", width=ancho, height=largo, command=lambda: press("x")).place(x=35,y=320)
Button(ventana, font=("arial",9,"bold"),text="/", width=ancho, height=largo, command=lambda: press("/")).place(x=105,y=320)
Button(ventana, font=("arial",9,"bold"),text="C", width=ancho, height=largo, command=clear).place(x=175,y=320)
Button(ventana, text="RESOLVER", width=28, height=2, command=resolver).place(x=35,y=380)



clear()

ventana.mainloop()