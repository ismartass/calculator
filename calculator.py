import tkinter as tk
from tkinter import messagebox


# functions
def add_numbers(numbers):
    value = display.get()
    value = value[:11]
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    display.delete(0, tk.END)
    display.insert(0, value + numbers)


def add_operation(operation):
    value = display.get()
    if value[-1] in '/*-+':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/':
        calculate()
        value = display.get()
    display.delete(0, tk.END)
    display.insert(0, value + operation)


def calculate():
    value = display.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    display.delete(0, tk.END)
    try:
        display.insert(0, eval(value))
    except (NameError, TypeError, SyntaxError):
        messagebox.showinfo('Attention!!!', 'Enter digit only!')
        display.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Attention!!!', 'Cannot  divide by zero!')
        display.insert(0, 0)


def clear():
    display.delete(0, tk.END)
    display.insert(0, 0)


def point_button(point):
    value = display.get()
    if '.' in value:
        pass
    elif '+-*/' in value[-1]:
        display.delete(0, tk.END)
        display.insert(0, value + point)
    else:
        display.delete(0, tk.END)
        display.insert(0, value + point)


# def add_minus():
#     value = display.get()
#     if '-' in value:
#         value = value[1:]
#     else:
#         display.delete(0, tk.END)
#         display.insert(0,  value)

# def percent(operation):
#     value = display.get()
#     if operation == '%':
#         operation = value / 100 *


# Buttons functions
def make_numb_button(number):
    return tk.Button(
        win, text=number, background='#2B2B2B', activebackground='#656566', fg='white', font=('Arial', 15),
        command=lambda: add_numbers(number)
    )


def make_operation_button(operation):
    return tk.Button(
        win, text=operation, bd=0, background='#f65904', activebackground='white', fg='white', font=('Arial', 15),
        command=lambda: add_operation(operation)
    )


def make_calc_button(operation):
    return tk.Button(
        win, text=operation, bd=0, background='#f65904', activebackground='white', fg='white', font=('Arial', 15),
        command=calculate)


def make_clear_button(operation):
    return tk.Button(
        win, text=operation, bd=0, background='grey', activebackground='white', fg='black', font=('Arial', 15),
        command=clear)


# def make_minus_button(special):
#     return tk.Button(
#         win, text=special, bd=0, background='grey', activebackground='white', fg='black', font=('Arial', 15),
#         command=add_minus()
#     )


# def make_percent_button(operation):
#     return tk.Button(
#         win, text=operation, bd=0, background='grey', activebackground='white', fg='black', font=('Arial', 15),
#         command=percent)

def make_point_button(point):
    return tk.Button(
        win, text=point, bd=0, background='#f65904', activebackground='white', fg='white', font=('Arial', 15),
        command=lambda: point_button(point)
    )


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_numbers(event.char)
    elif event.char in '/*-+':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


# создание окна и экрана
win = tk.Tk()
win.title('Calculator')
icon = tk.PhotoImage(file='icon.png')
win.config(bg='black')
win.iconphoto(False, icon)
win.geometry('240x350+550+200')
win.resizable(True, True)
win.maxsize(450, 500)
win.minsize(150, 200)

win.bind('<Key>', press_key)

display = tk.Entry(win, justify=tk.RIGHT, bd=0, background='black', fg='white', font=('Arial', 25), width=12)
display.insert(0, '0')

# расположение кнопок и экрана
display.grid(row=0, column=0, columnspan=4, stick='wens')
make_numb_button('7').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_numb_button('8').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_numb_button('9').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_numb_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_numb_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_numb_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_numb_button('1').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_numb_button('2').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_numb_button('3').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_numb_button('0').grid(row=5, column=0, columnspan=2, stick='wens', padx=5, pady=5)

make_point_button('.').grid(row=5, column=2, stick='wens', padx=5, pady=5)

make_operation_button('/').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('+').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=5, column=3, stick='wens', padx=5, pady=5)

make_clear_button('AC').grid(row=1, column=0, stick='wens', padx=5, pady=5)

# make_minus_button('+/-').grid(row=1, column=1, stick='wens', padx=5, pady=5)

# make_percent_button('%').grid(row=1, column=2, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
