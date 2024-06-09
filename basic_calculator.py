import re
import ast
from tkinter import *


# import parser
def get_variable(num):
    display.insert(END, num)


def get_operator(operator):
    display.insert(END, operator)


def clear_all():
    display.delete(0, END)


def calculate():
    curr_string = display.get()
    # elements = re.findall(r'(\d+|\(\d+\.\d+\)|\+|\-|\**|\/|\*)', curr_string)
    try:
        node = ast.parse(curr_string, mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        display.delete(0,END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def undo():
    mystr = display.get()
    if len(mystr):
        newstr = mystr[:-1]
        display.delete(0, END)
        display.insert(0, newstr)
    else:
        display.delete(0, END)

root = Tk()
root.title("Calculator")

# #  adding the input field
# tdisplay = Entry(root, font=("Arial", 12))
# tdisplay.grid(row=1, columnspan=6, sticky=W + E)

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

Button(root, text=".", width=4, font=("Arial", 12), command=lambda: get_variable('.')).grid(row=6, column=0, padx=5,
                                                                                            pady=5)
Button(root, text="0", width=4, font=("Arial", 12), command=lambda: get_variable(0)).grid(row=6, column=1, padx=5,
                                                                                          pady=5)
Button(root, text="=", width=4, font=("Arial", 12), command=lambda: calculate()).grid(row=6, column=2, padx=5,
                                                                                      pady=5)
Button(root, text="+", width=4, font=("Arial", 12), command=lambda: get_operator("+")).grid(row=3, column=3, padx=5,
                                                                                            pady=5)
Button(root, text="-", width=4, font=("Arial", 12), command=lambda: get_operator("-")).grid(row=4, column=3, padx=5,
                                                                                            pady=5)
Button(root, text="*", width=4, font=("Arial", 12), command=lambda: get_operator("*")).grid(row=5, column=3, padx=5,
                                                                                            pady=5)
Button(root, text="/", width=4, font=("Arial", 12), command=lambda: get_operator("/")).grid(row=6, column=3, padx=5,
                                                                                            pady=5)

Button(root, text="<<", width=4, font=("Arial", 12), command=lambda: undo()).grid(row=3, column=4, padx=5, pady=5)
Button(root, text="^2", width=4, font=("Arial", 12), command=lambda: get_operator("**2")).grid(row=4, column=4, padx=5,
                                                                                               pady=5)
Button(root, text="exp", width=4, font=("Arial", 12), command=lambda: get_operator("**")).grid(row=5, column=4, padx=5,
                                                                                               pady=5)
Button(root, text="CLR", width=4, font=("Arial", 12), command=lambda: clear_all()).grid(row=6, column=4, padx=5, pady=5)

# Button(root, text='(', width=4, font=("Arial", 12), command=lambda: get_variable('(')).grid(row=7, column=0, padx=5,
#                                                                                             pady=5)
# Button(root, text=')', width=4, font=("Arial", 12), command=lambda: get_variable(')')).grid(row=7, column=1, padx=5,
#                                                                                             pady=5)
root.minsize(width=300, height=220)
root.mainloop()
