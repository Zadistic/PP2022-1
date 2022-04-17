from tkinter import *

def dibujar1():

  coord = 20, 10, 20, 50
  line = C.create_line(coord)

  coord = 10, 20, 20, 10
  line = C.create_line(coord)

def dibujar2():

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

def dibujar3():

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


interfaz = Tk()

C = Canvas(interfaz, bg="white", height=250, width=300)

dibujar1()
dibujar2()
dibujar3()

C.pack()
mainloop()