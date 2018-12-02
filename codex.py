from tkinter import *

expression = ""

def press(num):
    global expression

    expression = expression = str(num)

    equation.set(expression)


gui = Tk()



gui.mainloop()