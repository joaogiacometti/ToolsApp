import random
import tkinter
from tkinter import *
from tkinter import messagebox as mb


def main():
    root = tkinter.Toplevel()

    def clear():
        nonlocal pc_number
        nonlocal user_number
        user_number = -1
        pc_number = random.randrange(11)
        user_guess.config(state='normal')
        try_button.config(state='normal')
        result.config(text='Resultado')
        pc_guess.config(text='?')

    def again():
        nonlocal pc_number
        pc_number = random.randrange(11)

    def validation():
        try:
            nonlocal user_number
            user_number = int(user_guess.get())
            if user_number > pc_number:
                result.config(text='Muito alto!')
            elif user_number < pc_number:
                result.config(text='Muito baixo!')
            elif user_number == pc_number:
                result.config(text='Você venceu!')
                user_guess.config(state='disabled')
                pc_guess.config(text=pc_number)
                try_button.config(state='disabled')
                again()
        except ValueError:
            mb.showerror(title='Erro', message='Você não digitou um número!')

    user_number = -1
    pc_number = random.randrange(11)

    root.title('Adivinhe o número')
    root.geometry('750x600')

    frame = Frame(root, width=750, height=600)
    frame.place(x=0, y=0)

    heading = Label(frame, text='Digite um número (0-10)!', font=('Arial', 28))
    heading.place(x=149, y=50, height=49, width=452)

    user_label = Label(frame, text='Você', font=('Arial', 32))
    user_label.place(x=130, y=164, width=97, height=43)

    user_guess = Entry(frame, font=('Arial', 23))
    user_guess.place(x=154, y=219, width=50, height=30)

    try_button = Button(frame, text='Tentar', font=('Arial', 23), bg='#61AEFF', command=validation)
    try_button.place(x=120, y=261)

    pc_label = Label(frame, text='Pc', font=('Arial', 32))
    pc_label.place(x=513, y=164, width=97, height=43)

    pc_guess = Label(frame, text='?', font=('Arial', 23))
    pc_guess.place(x=541, y=219, width=50, height=30)

    result = Label(frame, text='Resultado', font=('Arial', 28))
    result.place(x=101, y=433, height=76, width=534)

    again_button = Button(frame, text='resetar', bg='#61AEFF', command=lambda: clear(), font=('Arial', 23))
    again_button.place(x=230, y=519, width=276, height=59)

    root.mainloop()


if __name__ == '__main__':
    main()
