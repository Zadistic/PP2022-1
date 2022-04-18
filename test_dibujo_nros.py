from tkinter import *
def dibujar(numeros):

  if (numeros==1):
    coord = 20, 10, 20, 50
    line = C.create_line(coord)
    coord = 10, 20, 20, 10
    line = C.create_line(coord)
  if (numeros==2):
    coord = 40, 10, 60, 10
    line = C.create_line(coord)

    coord = 60, 10, 60, 30
    line = C.create_line(coord)

    coord = 60, 30, 40, 30
    line = C.create_line(coord)

    coord = 40, 30, 40, 50
    line = C.create_line(coord)

    coord = 40, 50, 60, 50
    line = C.create_line(coord)
  if (numeros==3):
    coord = 80, 10, 100, 10
    line = C.create_line(coord)

    coord = 100, 10, 100, 30
    line = C.create_line(coord)

    coord = 100, 30, 80, 30
    line = C.create_line(coord)

    coord = 100, 30, 100, 50
    line = C.create_line(coord)

    coord = 80, 10, 100, 10
    line = C.create_line(coord)

    coord = 100, 50, 80, 50
    line = C.create_line(coord)
  if (numeros==4):
    coord =120, 30,120 , 10
    line = C.create_line(coord)
    coord =120, 30,140 , 30
    line = C.create_line(coord)
    coord =140, 30,140 , 10
    line = C.create_line(coord)
    coord =140, 10,140 , 50
    line = C.create_line(coord)
  if (numeros==5):
    coord =150, 10,170 , 10
    line = C.create_line(coord)
    coord =150, 10,150 , 30
    line = C.create_line(coord)
    coord =150, 30,170 , 30
    line = C.create_line(coord)
    coord =170, 30,170 , 50
    line = C.create_line(coord)
    coord =170, 50,150 , 50
    line = C.create_line(coord)
  if (numeros==6):
    coord =180, 10,200 , 10
    line = C.create_line(coord)
    coord =180, 10,180 , 30
    line = C.create_line(coord)
    coord =180, 30,200 , 30
    line = C.create_line(coord)
    coord =200, 30,200 , 50
    line = C.create_line(coord)
    coord =200, 50,180 , 50
    line = C.create_line(coord)
    coord =180, 50,180 , 30
    line = C.create_line(coord)
  if (numeros==7):
    coord =210, 10,230 , 10
    line = C.create_line(coord)
    coord =230, 10,230 , 50
    line = C.create_line(coord)
  if (numeros==8):
    coord =240, 10,260 , 10
    line = C.create_line(coord)
    coord =240, 50,260 , 50
    line = C.create_line(coord)
    coord =240, 30,260 , 30
    line = C.create_line(coord)
    coord =240, 10,240 , 50
    line = C.create_line(coord)
    coord =260, 10,260 , 50
    line = C.create_line(coord)
  if (numeros==9):
    coord =10, 60,30 , 60
    line = C.create_line(coord)
    coord =10, 60,10 , 80
    line = C.create_line(coord)
    coord =10, 80,30 , 80
    line = C.create_line(coord)
    coord =30, 60,30 , 100
    line = C.create_line(coord)
  if (numeros==0):
    coord =40, 60,60 , 60
    line = C.create_line(coord)
    coord =40, 60,40 , 100
    line = C.create_line(coord)
    coord =60, 60,60 , 100
    line = C.create_line(coord)
    coord =40, 100,60 , 100
    line = C.create_line(coord)
    coord =40, 100,60 , 60
    line = C.create_line(coord)
  if (numeros==10):#suma
    coord =90, 60,90 , 100
    line = C.create_line(coord)
    coord =70, 80,110 , 80
    line = C.create_line(coord)
  if (numeros==11):#resta
    coord =130, 80,150 , 80
    line = C.create_line(coord)
  if (numeros==12): #multiplicacion
    coord =170, 75, 180, 85
    line = C.create_line(coord)
    coord =180, 75, 170, 85
    line = C.create_line(coord)
   
    
     
     

     
     



interfaz = Tk()

C = Canvas(interfaz, bg="white", height=250, width=300)

dibujar(1)
dibujar(2)
dibujar(3)
dibujar(4)
dibujar(5)
dibujar(6)
dibujar(7)
dibujar(8)
dibujar(9)
dibujar(0)
dibujar(10)
dibujar(11)
dibujar(12)
C.pack()
mainloop()