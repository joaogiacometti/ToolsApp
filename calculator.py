from tkinter import *


def main():
    def button_press(num):
        pass

    def equals():
        pass

    def clear():
        pass

    root = Tk()
    root.geometry('625x700')
    root.title('Calculadora')
    root.config(bg='#555050')

    equation_text = ''
    equation_label = StringVar()

    equation = Label(root, textvariable=equation_label, bg='black', fg='white')
    equation.place(x=25, y=33, width=575, height=100)

    frame = Frame(root, bg='red')
    frame.place(x=85, y=183, width=455, height=480)

    clear_btn = Button(frame, text='C', font=('Arial', 40), bg='black', fg='white')
    clear_btn.grid(row=0, column=0, columnspan=2)

    clear_btn = Button(frame, text='%', font=('Arial', 40), bg='black', fg='white')
    clear_btn.grid(row=2, column=3)



    root.mainloop()


main()
