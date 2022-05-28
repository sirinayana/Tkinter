import playsound
import tkinter as tk


def create_button(sound):
    return tk.Button(win, command=lambda: playsound.playsound(f'sounds/{sound}.mp3'), width=5, height=10, bg="black")


win = tk.Tk()
win.geometry("545x185")
win.title("Ксилофон")
win.resizable(0, 0)

create_button(1).grid(row=0, column=0)
create_button(2).grid(row=0, column=1)
create_button(3).grid(row=0, column=2)
create_button(4).grid(row=0, column=3)
create_button(5).grid(row=0, column=4)
create_button(6).grid(row=0, column=5)
create_button(7).grid(row=0, column=6)
create_button(8).grid(row=0, column=7)

win.mainloop()

