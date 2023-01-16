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

def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background color of the GUI window
    gui.configure(background="black")

    # set the titel of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create text entry box for showing expression
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing widgets at respective positions
    expression_field.grid(columnspan=4, ipadx = 70)

    # create a button and a place
    button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
                            command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)


    # start the GUI
    gui.mainloop()