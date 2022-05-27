import tkinter as tk


def next_pic():
    global counter
    counter += 1
    if counter > 6:
        counter = 1
    path = f"images/{str(counter)}.png"
    img["file"] = path


def previous_pic():
    global counter
    counter -= 1
    if counter < 1:
        counter = 6
    path = f"images/{str(counter)}.png"
    img["file"] = path


counter = 1

win = tk.Tk()
win.geometry("650x650")
win.resizable(0, 0)
win.title("Галерея")

main_label = tk.Label(win, text="Ваши фотографии:", font="Arial 24")
main_label.grid(row=0, column=0, columnspan=3, pady=20, stick="we")

img = tk.PhotoImage(file="images/1.png")
img_label = tk.Label(win, image=img)
img_label.grid(row=1, column=1)

button_next = tk.Button(text="->", font="Arial 16", command=next_pic)
button_next.grid(row=1, column=2, padx=10)
button_previous = tk.Button(text="<-", font="Arial 16", command=previous_pic)
button_previous.grid(row=1, column=0, padx=10)

win.mainloop()
