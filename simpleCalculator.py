from tkinter import *

expression = ""

def press(num):
    
    global expression

    # Concatenates string for view
    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    # Try and except use for division by zero

    try:
        global expression

        # eval function evaluates experession


        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error occurs then except handles
    except:
            equation.set(" error ")
            expression = ""