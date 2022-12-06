import tkinter
from tkinter import *
from time import *
from PIL import ImageTk


def main():
    def update():
        time_string = strftime("%H:%M:%S")
        time_label.config(text=time_string)
        time_label.after(1000, update)

    root = tkinter.Toplevel()

    # window.geometry("500x550")
    icon = ImageTk.PhotoImage(file="Images/clock.png")
    root.iconphoto(True, icon)
    root.configure(background="white")
    root.title("Relógio")
    root.resizable(False, False)

    time_label = Label(root, font="Arial, 50", fg="green", bg="black")
    time_label.pack(fill=BOTH, expand=True)

    update()
    root.mainloop()  # Display the window


if __name__ == '__main__':
    main()
