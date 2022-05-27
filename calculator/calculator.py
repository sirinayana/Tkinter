import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + str(digit))


def add_operation(operation):
    value = calc.get()
    try:
        if value[-1] in '+-*/':
            value = value[:-1]
        elif "+" in value or "-" in value or "*" in value or "/" in value:
            calculate()
            value = calc.get()
    except:
        value = "0"
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in "+-*/":
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo("Внимание", "На ноль делить нельзя")
    except:
        messagebox.showinfo("Внимание", "Неверный формат ввода")
        calc.insert(0, "0")


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, "0")


def del_last():
    value = len(calc.get())
    calc.delete(value - 1)


def make_digit_button(digit):
    return tk.Button(win, text=str(digit), bd=5, font=("Arial", 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(win, text=operation, bd=5, font=("Arial", 18, "bold"), command=lambda: add_operation(operation), fg="red")


def make_calc_button():
    return tk.Button(win, text="=", bd=5, font=("Arial", 18, "bold"), command=calculate, fg="white", bg="red")


def make_clear_button():
    return tk.Button(win, text="C", bd=5, font=("Arial", 18, "bold"), command=clear, fg="white", bg="red")


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == "=" or event.char == "\r":
        calculate()
    elif event.char == "\x08":
        del_last()


win = tk.Tk()
win.title("calculator")
win.geometry("240x270")
win["bg"] = "#33ffe6"
win.resizable(False, False)

win.bind("<Key>", press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="we")

make_digit_button(1).grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, stick="wens", padx=5, pady=5)

make_operation_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button("*").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button("/").grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_calc_button().grid(row=4, column=2, stick="wens", padx=5, pady=5)

make_clear_button().grid(row=4, column=1, stick="wens", padx=5, pady=5)

win.rowconfigure(1, minsize=60)
win.rowconfigure(2, minsize=60)
win.rowconfigure(3, minsize=60)
win.rowconfigure(4, minsize=60)

win.columnconfigure(0, minsize=60)
win.columnconfigure(1, minsize=60)
win.columnconfigure(2, minsize=60)
win.columnconfigure(3, minsize=60)

tk.mainloop()
