import tkinter as tk
import random as rd


def author_info(event):
    new_win = tk.Toplevel(win)
    new_win.title("Информация")
    new_win.geometry("400x50")
    new_win.resizable(0, 0)
    new_win["bg"] = "black"

    author_label = tk.Label(new_win, text="Автор: Яна Сирина", font="Arial 20", fg="white", bg="black")
    author_label.pack()


def set_cube():
    button_go['text'] = "Еще раз!"
    num = rd.randint(1, 6)
    path = f"images/{str(num)}.png"
    img["file"] = path

    try:
        user_num = int(guess_number.get())
        message_label["fg"] = "black"

        if user_num == num:
            message_label["fg"] = "green"
            message_label["text"] = "Отлично!"
        else:
            message_label["text"] = "Попробуй еще раз"

        guess_number.delete(0, tk.END)

    except:
        message_label["text"] = "Введите число!"
        message_label["fg"] = "red"
        guess_number.delete(0, tk.END)


def set_cube_event(event):
    set_cube()


def exit_button():
    win.destroy()


win = tk.Tk()
win.geometry("1000x800")
win.resizable(0, 0)
win.title("Игральные кости")

main_label = tk.Label(win, text="Игральная кость", font="Arial 24")
main_label.pack()
rules_label = tk.Label(win, text="Бросайте кость и угадвайте выпавшее число", font="Arial 16")
rules_label.pack()

img = tk.PhotoImage(file="images/1.png")
img_label = tk.Label(win, image=img)
img_label.pack()

message_label = tk.Label(win, text="Угадай число следующего броска:", font="Arial 18")
message_label.pack()
guess_number = tk.Entry(win, width=1, font="Arial 24")
guess_number.pack()

button_go = tk.Button(text="Играть!", font="Arial 20", command=set_cube)
button_go.pack()
button_stop = tk.Button(text="Выйти из игры", font="Arial 16", command=exit_button)
button_stop.pack()

win.bind("<Return>", set_cube_event)
win.bind("<Tab>", author_info)

win.mainloop()


