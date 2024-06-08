from tkinter import *

# import parser
pos = 0
flag = 0
operand1 =""
prev_operator = ""
result = ""

def get_variable(num):
    global pos
    global flag
    if flag:
        clear_disp()
        display.insert(pos, num)
        flag = 0
    else:
        display.insert(pos, num)
        pos += 1
def clear_all():
    global operand1

    clear_disp()
    tdisplay.delete(0, END)
    operand1 = ""
def clear_disp():
    global pos
    global tpos

    display.delete(0, END)
    pos = 0
    operand1 = ""

def calculate(oper1, oper2, oper):
    if oper == "+":
        return (oper1+oper2)
    elif oper == "-":
        return (oper1 - oper2)
    elif oper == "*":
        return (oper1 * oper2)
    elif oper == "/":
        return (oper1 / oper2)
    else:
        return ("not implemented yet!!")
def get_operator(operator):
    global pos
    global operand1
    global prev_operator
    global result
    global flag

    if operator == "+":
        if operand1 == "":
            operand1 = float(display.get())
            tdisplay.insert(END, display.get())
            tdisplay.insert(END, " + ")
            prev_operator = "+"
            clear_disp()

        else:
            result = calculate(float(display.get()), operand1, prev_operator)
            operand1 = result
            tdisplay.insert(END, display.get())
            tdisplay.insert(END, " + ")
            clear_disp()
            display.insert(0, result)
            flag = 1

def undo():
    global pos
    mystr = display.get()
    if len(mystr):
        newstr = mystr[:-1]
        tmp = pos-1
        clear_disp()
        display.insert(0, newstr)
        pos = tmp
    else:
        clear_disp()
        pos = 0

root = Tk()
root.title("Calculator")

#  adding the input field
tdisplay = Entry(root, font=("Arial", 12))
tdisplay.grid(row=1, columnspan=6, sticky=W + E)

display = Entry(root, font=("Arial", 14), borderwidth=3)
display.grid(row=2, columnspan=6, sticky=W + E)

# adding buttons

Button(root, text="1", width=4, font=("Arial", 12), command=lambda: get_variable(1)).grid(row=3, column=0, padx=5,
                                                                                          pady=5)
Button(root, text="2", width=4, font=("Arial", 12), command=lambda: get_variable(2)).grid(row=3, column=1, padx=5,
                                                                                          pady=5)
Button(root, text="3", width=4, font=("Arial", 12), command=lambda: get_variable(3)).grid(row=3, column=2, padx=5,
                                                                                          pady=5)

Button(root, text="4", width=4, font=("Arial", 12), command=lambda: get_variable(4)).grid(row=4, column=0, padx=5,
                                                                                          pady=5)
Button(root, text="5", width=4, font=("Arial", 12), command=lambda: get_variable(5)).grid(row=4, column=1, padx=5,
                                                                                          pady=5)
Button(root, text="6", width=4, font=("Arial", 12), command=lambda: get_variable(6)).grid(row=4, column=2, padx=5,
                                                                                          pady=5)

Button(root, text="7", width=4, font=("Arial", 12), command=lambda: get_variable(7)).grid(row=5, column=0, padx=5,
                                                                                          pady=5)
Button(root, text="8", width=4, font=("Arial", 12), command=lambda: get_variable(8)).grid(row=5, column=1, padx=5,
                                                                                          pady=5)
Button(root, text="9", width=4, font=("Arial", 12), command=lambda: get_variable(9)).grid(row=5, column=2, padx=5,
                                                                                          pady=5)

Button(root, text=".", width=4, font=("Arial", 12), command=lambda: get_variable('.')).grid(row=6, column=0, padx=5, pady=5)
Button(root, text="0", width=4, font=("Arial", 12), command=lambda: get_variable(0)).grid(row=6, column=1, padx=5,
                                                                                          pady=5)
Button(root, text="=", width=4, font=("Arial", 12)).grid(row=6, column=2, padx=5, pady=5)

Button(root, text="+", width=4, font=("Arial", 12), command=lambda: get_operator("+")).grid(row=3, column=3, padx=5, pady=5)
Button(root, text="-", width=4, font=("Arial", 12), command=lambda: get_operator("-")).grid(row=4, column=3, padx=5, pady=5)
Button(root, text="*", width=4, font=("Arial", 12), command=lambda: get_operator("*")).grid(row=5, column=3, padx=5, pady=5)
Button(root, text="/", width=4, font=("Arial", 12), command=lambda: get_operator("/")).grid(row=6, column=3, padx=5, pady=5)

Button(root, text="<<", width=4, font=("Arial", 12), command=lambda: undo()).grid(row=3, column=4, padx=5, pady=5)
Button(root, text="sqr", width=4, font=("Arial", 12), command=lambda: get_operator("sqr")).grid(row=4, column=4, padx=5, pady=5)
Button(root, text="exp", width=4, font=("Arial", 12), command=lambda: get_operator("**")).grid(row=5, column=4, padx=5, pady=5)
Button(root, text="CLR", width=4, font=("Arial", 12), command=lambda: clear_all()).grid(row=6, column=4, padx=5, pady=5)

root.minsize(width=300, height=220)
root.mainloop()
