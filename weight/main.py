import tkinter as tk
from tkinter import messagebox


def func():
    if r_var.get() == 0:
        try:
            height_label['fg'] = 'black'
            weight = int(height_entry.get()) - 110
            messagebox.showinfo("Результат", "Ваш идеальный вес = " + str(weight))
            height_entry.delete(0, tk.END)
        except:
            height_label['fg'] = 'red'
    elif r_var.get() == 1:
        try:
            height_label['fg'] = 'black'
            weight = int(height_entry.get()) - 100
            messagebox.showinfo("Результат", "Ваш идеальный вес = " + str(weight))
            height_entry.delete(0, tk.END)
        except:
            height_label['fg'] = 'red'


win = tk.Tk()
win.title("Расчет идеального веса")
win.geometry("350x200")
win.resizable(0, 0)

main_label = tk.Label(win, text="Рассчитайте свой идеальный вес!", font="Arial 14")
main_label.pack()

gender_label = tk.Label(win, text="Выберете ваш пол:", font="Arial 12")
gender_label.pack()

r_var = tk.BooleanVar()
r_var.set(0)
r1 = tk.Radiobutton(text='Муж.', variable=r_var, value=0)
r2 = tk.Radiobutton(text='Жен.', variable=r_var, value=1)
r1.pack()
r2.pack()

height_label = tk.Label(win, text="Введите ваш рост (в см):", font="Arial 12")
height_label.pack()

height_entry = tk.Entry(win, font="Arial 12", width=3)
height_entry.pack()

result_button = tk.Button(win, text="Рассчитать", command=func)
result_button.pack(pady=8)

win.mainloop()
