from tkinter import *

#параметры поля
cell_size = 60
x_count = 4
y_count = 4

#массив игровых элементов
elems = ["e1", "e2", "e2","e3","e4","e5","e6","e7", "e8","e8","e9","e10","e11", "e12","e13","e14","e15","e0"]

root = Tk()
root.title("Пятнашки")

canv = Canvas()
canv.pack()

root.mainloop()
