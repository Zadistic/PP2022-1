from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.tix import COLUMN

x=20
y1=10
y2=50
i=x
contadori=x
contadorf=x
op_color = "black"
num_color = "black"
prev_selec = "empty"

def color_change(color):

    global op_color, num_color

    if color == "black":
        op_color = "black"
        num_color = "black"

    elif color == "pink":
        op_color = "#ff00aa"
        num_color = "#ff00aa"

    elif color == "purple":
        op_color = "purple"
        num_color = "purple"

    elif color == "orange":
        op_color = "orange"
        num_color = "orange"

    elif color == "cyan":
        op_color = "cyan"
        num_color = "cyan"

    elif color == "green":
        op_color = "green"
        num_color = "green"

    elif color == "yellow":
        op_color = "yellow"
        num_color = "yellow"

    elif color == "dark_red":
        op_color = "dark red"
        num_color = "dark red"

    elif color == "light_blue":
        op_color = "#0099ad"
        num_color = "#0099ad"

    elif color == "red":
        op_color = "red"
        num_color = "red"

    elif color == "light_green":
        op_color = "#4dff00"
        num_color = "#4dff00"

    elif color == "blue":
        op_color = "blue"
        num_color = "blue"

def fraccion(numeros): 

    global i, y1, y2, contadori, contadorf

    if prev_selec != "empty":

        coord = contadori, y1+45, i, y2+5
        dibujo.create_line(coord, fill=op_color, width=4)
        dibujo.addtag_all

        y1 = 65
        y2 = 105

        i = contadori
        contadorf = i

        text_square.insert(i, numeros)

    else:
        return 0

def dibujar(numeros):
   
    global y1, y2, i, contadori, contadorf, prev_selec

    if (numeros == 0): #Nro 0
        
        if prev_selec == "^":

            #0 Pequeño
            coord =i, y1-5, i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1-5, i , y2-35
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1+5, i+5 , y2-35
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1+5, i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1+5, i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)

            prev_selec = 0

        else:
            
            coord =i, y1, i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+40, i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+40, i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1,i , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1, i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all

            prev_selec = 0

    elif (numeros == 1): #Nro 1

        if prev_selec == "^":

            #1 chiquito
            coord = i, y1-5, i, y2-30
            dibujo.create_line(coord, fill=num_color, width=2)
            dibujo.addtag_all

            prev_selec = 1
        
        else:

            coord = i+10, y1, i+10, y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all

            prev_selec = 1

    elif (numeros == 2): #Nro 2
        
        if prev_selec == "^":

            #2 chiquito
            coord = i, y1-5, i+5, y2-45
            dibujo.create_line(coord, fill=num_color)
            coord = i+5, y1-5, i+5, y2-42
            dibujo.create_line(coord, fill=num_color)
            coord = i+5, y1-2, i, y2-42
            dibujo.create_line(coord, fill=num_color)
            coord = i, y1-2, i, y2-39
            dibujo.create_line(coord, fill=num_color)
            coord = i, y1+1, i+5, y2-39
            dibujo.create_line(coord, fill=num_color)
            dibujo.addtag_all

        else:

            coord = i, y1, i+20, y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i+20, y1, i+20, y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i+20, y1+20, i, y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i, y1+20, i, y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i, y1+40, i+20, y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all

        prev_selec = 2
        
    elif (numeros == 3): #Nro 3

        if prev_selec == "^":

            #3 chiquito
            coord = i, y1-5, i+5, y2-45
            dibujo.create_line(coord, fill=num_color)
            coord = i+5, y1-5, i+5, y2-42
            dibujo.create_line(coord, fill=num_color)
            coord = i+5, y1-2, i, y2-42
            dibujo.create_line(coord, fill=num_color)
            coord = i+5, y1-5, i+5, y2-39
            dibujo.create_line(coord, fill=num_color)
            coord = i+5, y1+1, i, y2-39
            dibujo.create_line(coord, fill=num_color)
        
        else:

            coord = i, y1, i+20, y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i+20, y1, i+20, y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i+20, y1+20, i, y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i+20, y1+20, i+20, y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i, y1, i+20, y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord = i+20, y1+40, i, y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all
        
        prev_selec = 3

    elif (numeros == 4): #Nro 4

        if prev_selec == "^":

            #4 chiquito
            coord =i, y1-5,i , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1,i+5 , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1-5,i+5 , y2-35
            dibujo.create_line(coord, fill=num_color)
        
        else:

            coord =i, y1+20,i , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+20,i+20 , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1+20,i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all
        
        prev_selec = 4

    elif (numeros == 5): #Nro 5

        if prev_selec =="^":

            #5 chiquito
            coord =i, y1-5,i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1-5,i , y2-42
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1-2,i+5 , y2-42
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1-2,i+5 , y2-39
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1+1,i , y2-39
            dibujo.create_line(coord, fill=num_color)

        else:

            coord =i, y1,i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1,i , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+20,i+20 , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1+20,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1+40,i , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all

        prev_selec = 5
        
    elif (numeros == 6): #Nro 6

        if prev_selec == "^":

            #6 chiquito
            coord =i, y1-5 ,i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1-5 ,i , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1 ,i+5 , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1 ,i+5 , y2-35
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1+5 ,i , y2-35
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1+5 ,i , y2-40
            dibujo.create_line(coord, fill=num_color)

        else:

            coord =i, y1 ,i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1 ,i , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+40 ,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1+40,i+20 , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+20,i+20, y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all
        
        prev_selec = 6

    elif (numeros == 7): #Nro 7

        if prev_selec == "^":

            #7 chiquito
            coord =i, y1-5,i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1-5,i+5 , y2-38
            dibujo.create_line(coord, fill=num_color)
        
        else:

            coord =i, y1,i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all
        
        prev_selec = 7

    elif (numeros == 8): #Nro 8

        if prev_selec == "^":

            #8 chiquito
            coord =i, y1-5,i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1-5,i , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1,i+5 , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1-5,i+5 , y2-35
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1+5,i , y2-35
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1+5,i , y2-40
            dibujo.create_line(coord, fill=num_color)
            dibujo.addtag_all

        else:

            coord =i, y1,i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+40,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+20,i+20 , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1,i , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all
        
        prev_selec = 8
        
    elif (numeros == 9): #Nro 9

        if prev_selec == "^":

            #9 chiquito
            coord =i, y1-5,i+5 , y2-45
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1-5,i , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i, y1,i+5 , y2-40
            dibujo.create_line(coord, fill=num_color)
            coord =i+5, y1-5,i+5 , y2-35
            dibujo.create_line(coord, fill=num_color)
        
        else:

            coord =i, y1,i , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1+20,i+20 , y2-20
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i+20, y1,i+20 , y2
            dibujo.create_line(coord, fill=num_color, width=3)
            coord =i, y1,i+20 , y2-40
            dibujo.create_line(coord, fill=num_color, width=3)
            dibujo.addtag_all

        prev_selec = 9

    elif (numeros == "+"): #Suma
        
        if prev_selec != "empty" and prev_selec != "+" and prev_selec != "*" and prev_selec != "(" and prev_selec != "^":
            
            y1 = 10
            y2 = 50

            coord =i+10, y1, i+10 , y2-10
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i, y1+15, i+20 , y2-25
            dibujo.create_line(coord, fill=op_color, width=3)
            dibujo.addtag_all
            prev_selec = "+"
            contadori=i+30
        
        else:
            return 0

    elif (numeros == "-"): #Resta

        if prev_selec != "empty" and prev_selec != "-" and prev_selec != "*" and prev_selec != "^":

            y1 = 10
            y2 = 50

            coord =i, y1+20,i+20 , y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            dibujo.addtag_all
            contadori=i+30

            prev_selec = "-"

        else:
            return 0
        
    elif (numeros == "*"): #Multiplicacion
        
        if prev_selec != "empty" and prev_selec != "*" and prev_selec != "+" and prev_selec != "-" and prev_selec != "^":

            y1 = 10
            y2 = 50
            
            coord =i, y1+10, i+10, y2-15
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+10, y1+10, i, y2-15
            dibujo.create_line(coord, fill=op_color, width=3)
            dibujo.addtag_all
            contadori=i+30

            prev_selec = "*"

        else:
            return 0

    if (numeros =="^"): #Potencia

        prev_selec = "^"
        i=i-30

    elif (numeros == "!"): #Factorial

        if (prev_selec != "sen(" and prev_selec != "cos(" and prev_selec != "tan(" and 
        prev_selec != "(" and prev_selec != "empty" and prev_selec != "+" and prev_selec != "-" and prev_selec != "*"):

            #recta vertical
            coord =i+3, y1,i+3 , y2-10
            dibujo.create_line(coord, fill=op_color, width=3)
            #punto
            coord=i,y1+40,i+5,y2-5
            dibujo.create_oval(coord,fill=op_color, width=1)
            dibujo.addtag_all

            prev_selec = "!"
        
        else:
            return 0

    elif (numeros == "sen("): #Seno 

        if (prev_selec == 1 or prev_selec == 2 or prev_selec == 3 or prev_selec == 4 or prev_selec == 5 or prev_selec == 6 
        or prev_selec == 7 or prev_selec == 8 or prev_selec == 9 or prev_selec == 0):

            return 0

        else:

            #S
            coord =i, y1,i+20 , y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i, y1,i, y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i, y1+20,i+20, y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+20, y1+20,i+20, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+20, y1+40,i, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            #E
            coord =i+25, y1,i+45, y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+25, y1,i+25, y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+25, y1+20,i+45, y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+25, y1+20,i+25, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+25, y1+40,i+45, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            #N
            coord =i+50, y1,i+50, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+50, y1,i+75, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+75, y1,i+75, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            #(
            coord=i+90,y1-5,i+80,y2-35
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+80,y1+5,i+80,y2-5
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+80,y1+35,i+90,y2+5
            dibujo.create_line(coord,fill=op_color, width=3)
            
            dibujo.addtag_all
            i=i+60

            prev_selec = "sen("
    
    elif (numeros == "cos("): #Coseno

        if (prev_selec == 1 or prev_selec == 2 or prev_selec == 3 or prev_selec == 4 or prev_selec == 5 or prev_selec == 6 
        or prev_selec == 7 or prev_selec == 8 or prev_selec == 9 or prev_selec == 0):

            return 0

        else:

            #C
            coord =i, y1,i+20 , y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            coord=i,y1,i,y2
            dibujo.create_line(coord,fill=op_color, width=3)
            coord =i, y1+40,i+20 , y2
            dibujo.create_line(coord, fill=op_color, width=3)
            #O
            coord =i+25, y1, i+45 , y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+25, y1+40, i+45 , y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+25, y1,i+25 , y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+45, y1, i+45 , y2
            dibujo.create_line(coord, fill=op_color, width=3)
            #S
            coord =i+50, y1,i+70 , y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+50, y1,i+50, y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+50, y1+20,i+70, y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+70, y1+20,i+70, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+70, y1+40,i+50, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            dibujo.addtag_all
            #(
            coord=i+85,y1-5,i+75,y2-35
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+75,y1+5,i+75,y2-5
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+75,y1+35,i+85,y2+5
            dibujo.create_line(coord,fill=op_color, width=3)
            dibujo.addtag_all
            i=i+60

            prev_selec = "cos("

    elif (numeros == "tan("): #Tangente

        if (prev_selec == 1 or prev_selec == 2 or prev_selec == 3 or prev_selec == 4 or prev_selec == 5 or prev_selec == 6 
        or prev_selec == 7 or prev_selec == 8 or prev_selec == 9 or prev_selec == 0):

            return 0

        else:

            #T
            coord =i+15, y1,i+15 , y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i, y1,i+30 , y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            #A
            coord =i+30, y1+40,i+40 , y2-40
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+40, y1,i+50 , y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+35, y1+20,i+45 , y2-20
            dibujo.create_line(coord, fill=op_color, width=3)
            #N
            coord =i+52, y1,i+52, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+52, y1,i+77, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            coord =i+77, y1,i+77, y2
            dibujo.create_line(coord, fill=op_color, width=3)
            #(
            coord=i+92,y1-5,i+82,y2-35
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+82,y1+5,i+82,y2-5
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+82,y1+35,i+92,y2+5
            dibujo.create_line(coord,fill=op_color, width=3)
            dibujo.addtag_all

            i=i+60

            prev_selec == "tan("

    elif (numeros == "("): #Abre Parentesis

        if prev_selec != "sen(" and prev_selec != "cos(" and prev_selec != "tan(":
            coord=i+10,y1-5,i,y2-35
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i,y1+5,i,y2-5
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i,y1+35,i+10,y2+5
            dibujo.create_line(coord,fill=op_color, width=3)
            dibujo.addtag_all
            i=i-20

            prev_selec = "("

        else:
            return 0

    elif (numeros == ")"): #Cierre parentesis

        if prev_selec != "(" and prev_selec != "empty":
            i=i-10
            coord=i,y1-5,i+10,y2-35
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+10,y1+5,i+10,y2-5
            dibujo.create_line(coord,fill=op_color, width=3)
            coord=i+10,y1+35,i,y2+5
            dibujo.create_line(coord,fill=op_color, width=3)
            dibujo.addtag_all
        
            prev_selec = ")"
        
        else:
            return 0

    elif (numeros == "√"): #Raiz

        coord =i, y1+20,i+10, y2
        dibujo.create_line(coord, fill=op_color, width=3)
        coord =i+10, y1+40,i+15, y2-45
        dibujo.create_line(coord, fill=op_color, width=3)
        coord =i+15, y1-5,i+25, y2-45
        dibujo.create_line(coord, fill=op_color, width=3)

        dibujo.addtag_all

    i=i+30
    contadorf=contadorf+30
    text_square.insert(i, numeros)

def limpiar():

    global i, y1, y2, contadori, contadorf, prev_selec
    
    text_square.delete(0, 'end')
    dibujo.delete("all")
    
    i=x
    contadorf=x
    contadori=x
    y1 = 10
    y2 = 50
    prev_selec = "empty"
	 
interfaz = Tk()
interfaz.configure(background="#616161")
interfaz.title("CALCULADORA")
interfaz.minsize()
fontStyle = tkFont.Font(family="Lucida Grande", size=22)

fila_base = 4
altura = 1
ancho = 10

dibujo = Canvas(interfaz, bg="#dbdbdb")
dibujo.grid(columnspan=8, ipadx=349, ipady=30, row= fila_base-3, column=0)

text_square = Entry(interfaz, width=70, font =("Lucida Grande", 20), bg="#dbdbdb", fg=num_color)
text_square.grid(columnspan=8, pady=10, ipady= 4, row= fila_base-2, column=0)

#BOTONES COLORES

black_color = Button(interfaz, bg= "black",
command= lambda:color_change("black"), height=altura+2, width=7)
black_color.grid(row= fila_base+1, column=5)
pink_color = Button(interfaz, bg= "#ff00aa",
command= lambda:color_change("pink"), height=altura+2, width=7)
pink_color.grid(row= fila_base+1, column=6)
purple_color = Button(interfaz, bg= "purple",
command= lambda:color_change("purple"), height=altura+2, width=7)
purple_color.grid(row= fila_base+1, column=7)

orange_color = Button(interfaz, bg= "orange",
command= lambda:color_change("orange"), height=altura+2, width=7)
orange_color.grid(row= fila_base+2, column=5)
cyan_color = Button(interfaz, bg= "cyan",
command= lambda:color_change("cyan"), height=altura+2, width=7)
cyan_color.grid(row= fila_base+2, column=6)
green_color = Button(interfaz, bg= "green",
command= lambda:color_change("green"), height=altura+2, width=7)
green_color.grid(row= fila_base+2, column=7)

yellow_color = Button(interfaz, bg= "yellow",
command= lambda:color_change("yellow"), height=altura+2, width=7)
yellow_color.grid(row= fila_base+3, column=5)
burdeo_color = Button(interfaz, bg= "dark red",
command= lambda:color_change("dark_red"), height=altura+2, width=7)
burdeo_color.grid(row= fila_base+3, column=6)
light_blue_color = Button(interfaz, bg= "#0099ad",
command= lambda:color_change("light_blue"), height=altura+2, width=7)
light_blue_color.grid(row= fila_base+3, column=7)

red_color = Button(interfaz, bg= "red",
command= lambda:color_change("red"), height=altura+2, width=7)
red_color.grid(row= fila_base+4, column=5)
light_green_color = Button(interfaz, bg= "#4dff00",
command= lambda:color_change("light_green"), height=altura+2, width=7)
light_green_color.grid(row= fila_base+4, column=6)
blue_color = Button(interfaz, bg= "blue",
command= lambda:color_change("blue"), height=altura+2, width=7)
blue_color.grid(row= fila_base+4, column=7)

#Botón para número 1
case1 = Button(interfaz, text=" 1 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(1), height=altura, width=ancho)
case1.grid(row=fila_base+3, column=1)

#Botón para número 2
case2 = Button(interfaz, text=" 2 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(2), height=altura, width=ancho)
case2.grid(row=fila_base+3, column=2)

#Botón para número 3
case3 = Button(interfaz, text=" 3 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(3), height=altura, width=ancho)
case3.grid(row=fila_base+3, column=3)

#Botón para número 4
case4 = Button(interfaz, text=" 4 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(4), height=altura, width=ancho)
case4.grid(row=fila_base+2, column=1)

#Botón para número 5
case5 = Button(interfaz, text=" 5 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(5), height=altura, width=ancho)
case5.grid(row=fila_base+2, column=2)

#Botón para número 6
case6 = Button(interfaz, text=" 6 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(6), height=altura, width=ancho)
case6.grid(row=fila_base+2, column=3)

#Botón para número 7
case7 = Button(interfaz, text=" 7 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(7), height=altura, width=ancho)
case7.grid(row=fila_base+1, column=1)

#Botón para número 8
case8 = Button(interfaz, text=" 8 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(8), height=altura, width=ancho)
case8.grid(row=fila_base+1, column=2)

#Botón para número 9
case9 = Button(interfaz, text=" 9 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(9), height=altura, width=ancho)
case9.grid(row=fila_base+1, column=3)

#Botón para número 0
case0 = Button(interfaz, text=" 0 ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar(0), height=altura, width=ancho)
case0.grid(row=fila_base+4, column=1)

#Botón para operador +
suma = Button(interfaz, text=" + ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar("+"), height=altura, width=ancho)
suma.grid(row=fila_base+1, column=4)

#Botón para operador -
resta = Button(interfaz, text=" — ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar("-"), height=altura, width=ancho)
resta.grid(row=fila_base+2, column=4)

#Botón para operador X
multip = Button(interfaz, text=" X ", font= fontStyle, fg="white", bg="grey39",
command=lambda: dibujar("*"), height=altura, width=ancho)
multip.grid(row=fila_base+3, column=4)

#Botón para operador /
division = Button(interfaz, text=" / ", font= fontStyle, fg="white", bg="grey39",
command=lambda: fraccion("/"), height=altura, width=ancho)
division.grid(row=fila_base+4, column=4)

#Botón para operador =
resol = Button(interfaz, text=" = ", font= fontStyle, fg="white", bg="grey39",
height=altura, width=ancho)
resol.grid(row=fila_base+4, column=3)

#Botón para VACIAR
vaciar = Button(interfaz, text=" CE ", relief=FLAT, font= fontStyle, fg="white", bg="#611115",
command=limpiar, height=altura, width=ancho)
vaciar.grid(row=fila_base, column=4)

#Botón para operador factorial
fact = Button(interfaz, text=" x! ", font = fontStyle, fg= "white", bg="grey39",
command=lambda:dibujar("!"), height=altura, width=ancho)
fact.grid(row=fila_base, column=0)

#Botón para operador seno
seno = Button(interfaz, text=" sen ", font = fontStyle, fg= "white", bg="grey39",
command=lambda:dibujar("sen("), height=altura, width=ancho)
seno.grid(row=fila_base+1, column=0)

#Botón para operador coseno
coseno = Button(interfaz, text=" cos ", font = fontStyle, fg= "white", bg="grey39",
command=lambda:dibujar("cos("), height=altura, width=ancho)
coseno.grid(row=fila_base+2, column=0)

#Botón para operador tangente
tang = Button(interfaz, text=" tan ", font = fontStyle, fg= "white", bg="grey39",
command=lambda:dibujar("tan("), height=altura, width=ancho)
tang.grid(row=fila_base+3, column=0)

#Botón para operador potencia
potencia = Button(interfaz, text=" x² ", font = fontStyle, fg= "white", bg="grey39",
command = lambda:dibujar("^"), height=altura, width=ancho)
potencia.grid(row=fila_base+4, column=0)

#Botón para operador decimal
decimal = Button(interfaz, text=" . ", font = fontStyle, fg="white", bg="grey39",
command = lambda:dibujar("."), height=altura, width=ancho)
decimal.grid(row=fila_base+4, column=2)

#Botón para operador raiz
raiz = Button(interfaz, text=" √ ", font = fontStyle, fg= "white", bg="grey39",
command=lambda:dibujar("√"), height=altura, width=ancho)
raiz.grid(row=fila_base, column=2)

#Botón para Abre Paréntesis
abreP = Button(interfaz, text=" ( ", font = fontStyle, fg="white", bg="grey39",
command = lambda:dibujar("("), height=altura, width=ancho)
abreP.grid(row=fila_base, column= 1)

#Botón para Cierre Paréntesis
cierreP = Button(interfaz, text=" ) ", font = fontStyle, fg="white", bg="grey39",
command = lambda:dibujar(")"), height=altura, width=ancho)
cierreP.grid(row =fila_base, column= 3)

#Botón para Activar Coordenadas
coords = Button(interfaz, text=" coords", font=fontStyle, fg="white", bg="grey39", width=ancho)
coords.grid(row=fila_base, column=5, columnspan=3)

interfaz.mainloop()