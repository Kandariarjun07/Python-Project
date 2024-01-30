from tkinter import *

expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" Error ") 
        expression = "" 

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

if __name__ == "__main__":
    gui = Tk()
    gui.title("Calculator")
    gui.geometry("400x350")
    gui.resizable(False, False)
    gui.configure(bg="Black")

    equation = StringVar()
    

    exp = Entry(gui, width=30, textvariable=equation, font=('Arial', 16, 'bold'))
    exp.grid(columnspan=5, ipadx=30, ipady=10)

    button_font = ('Arial', 16, 'bold')
    button_style = {'bg': 'black', 'fg': 'white', 'height': 1, 'width': 7, 'borderwidth': 0, 'font': button_font}

    b1 = Button(gui, text='1', command=lambda: press(1), **button_style)
    b1.grid(row=2, column=0, pady=20)

    b2 = Button(gui, text='2', command=lambda: press(2), **button_style)
    b2.grid(row=2, column=1)

    b3 = Button(gui, text='3', command=lambda: press(3), **button_style)
    b3.grid(row=2, column=2)

    b4 = Button(gui, text='4', command=lambda: press(4), **button_style)
    b4.grid(row=4, column=0, pady=20)

    b5 = Button(gui, text='5', command=lambda: press(5), **button_style)
    b5.grid(row=4, column=1)

    b6 = Button(gui, text='6', command=lambda: press(6), **button_style)
    b6.grid(row=4, column=2)

    b7 = Button(gui, text='7', command=lambda: press(7), **button_style)
    b7.grid(row=6, column=0, pady=20)

    b8 = Button(gui, text='8', command=lambda: press(8), **button_style)
    b8.grid(row=6, column=1)

    b9 = Button(gui, text='9', command=lambda: press(9), **button_style)
    b9.grid(row=6, column=2)
    
    # Number 0
    zero_button = Button(gui, text='0', command=lambda: press('0'), **button_style)
    zero_button.grid(row=8, column=0,pady=20)

    operators = ['+', '-', '*', '/']
    for i, operator in enumerate(operators):
        operator_button = Button(gui, text=operator, command=lambda : press(operator), **button_style)
        operator_button.grid(row=i * 2 + 2, column=3)

    clear_button = Button(gui, text="Clear", command=clear, **button_style)
    clear_button.grid(row=8, column=1)

    equal_button = Button(gui, text="=", command=equal, **button_style)
    equal_button.grid(row=8, column=2)

    gui.mainloop()
