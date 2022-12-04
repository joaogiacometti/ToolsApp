from tkinter import *
import calculator

# Variables
root = Tk()

root.title('Menu')
root.geometry('750x500')
root.resizable(False, False)

frame = Frame(root, width=750, height=500)
frame.place(x=0, y=0)

user = Label(frame, text='Bem vindo!', font=('Arial', 23))
user.place(x=18, y=24)

heading = Label(frame, text='Ferramentas', font=('Arial', 28))
heading.place(x=260, y=106, width=236, height=50)

btn_calculadora = Button(frame, text='Calculadora', border=0, bg='black', fg='white')
btn_calculadora.place(x=272, y=208, width=202, height=41)

clock = Button(frame, text='Relógio', border=0, bg='black', fg='white')
clock.place(x=272, y=292, width=202, height=41)

guess = Button(frame, text='Adivinhe o número', border=0, bg='black', fg='white')
guess.place(x=272, y=376, width=202, height=41)

root.mainloop()
