
from tkinter import *

window = Tk()
window.iconbitmap("assets/img/calculadora.ico")
window.title("Calculadora")

# Definição das cores
color1 = "#363636"
color2 = "#000000"
color3 = "#ff0000"
color4 = "#DCDCDC"
color5 = "#FF0000"
color6 = "#FFFFFF"
color7 = "#FFFFFF"

frameDisplay = Frame(window, width=323, height=120, bg=color2)
frameDisplay.grid(row=0, column=0)

frameKeyboard = Frame(window, width=323, height=250, bg=color1)
frameKeyboard.grid(row=1, column=0)

frameFooter = Frame(window, width=323, height=15, bg=color1)
frameFooter.grid(row=2, column=0)

showValue = StringVar()
values = ''

def inputValue(event):
    global values
    values += str(event)
    showValue.set(values)

def calculate():
    global values
    try:
        result = eval(values)
        showValue.set(str(result))
        values = str(result)
    except Exception as e:
        showValue.set("comando invalido")
        values = ''

def clean():
    global values
    values = ''
    showValue.set('')

# Label
labelScreen = Label(frameDisplay, textvariable=showValue, bg=color1, fg=color2, font=("Ivy", 24, "bold"), width=16, padx=8, pady=40, justify="right", anchor="e", relief="flat")
labelScreen.pack()

labelFooter = Label(frameFooter, text="V.: 0.1.0", bg=color1, fg=color2, font=("Ivy", 9), width=44, padx=8, justify="right", anchor="e")
labelFooter.pack()

# Botões
btn1 = Button(frameKeyboard, command=clean, text="Delete", width=17, height=2, bg=color3, fg=color2, font=("Ivy", 11, "bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0)
btn1.place(x=0, y=0)

# Botões 2 a 18
buttons = [
    ('%', lambda: inputValue('%'), 162, 0),
    ('/', lambda: inputValue('/'), 243, 0),
    ('7', lambda: inputValue('7'), 0, 49),
    ('8', lambda: inputValue('8'), 81, 49),
    ('9', lambda: inputValue('9'), 162, 49),
    ('x', lambda: inputValue('*'), 243, 49),
    ('4', lambda: inputValue('4'), 0, 98),
    ('5', lambda: inputValue('5'), 81, 98),
    ('6', lambda: inputValue('6'), 162, 98),
    ('-', lambda: inputValue('-'), 243, 98),
    ('1', lambda: inputValue('1'), 0, 147),
    ('2', lambda: inputValue('2'), 81, 147),
    ('3', lambda: inputValue('3'), 162, 147),
    ('+', lambda: inputValue('+'), 243, 147),
    ('0', lambda: inputValue('0'), 0, 196),
    ('.', lambda: inputValue('.'), 162, 196),
    ('=', calculate, 243, 196),
]

for (text, command, x, y) in buttons:
    btn = Button(frameKeyboard, command=command, text=text, width=8 if text != '0' else 17, height=2, bg=color4, fg=color2, font=("Ivy", 11), relief="flat", overrelief="raised", activebackground=color3, activeforeground=color2, highlightthickness=0, borderwidth=0)
    btn.place(x=x, y=y)

window.mainloop()
