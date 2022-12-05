from tkinter import *


def main():
    equation_text = ''

    def button_press(num):
        nonlocal equation_text
        equation_text = equation_text + str(num)
        equation_label.set(equation_text)

    def equals():
        nonlocal equation_text

        try:
            result = str(eval(equation_text))  # Eval é usado para realizar equações
            equation_label.set(result)
            equation_text = result

        except ZeroDivisionError:
            equation_label.set('Erro aritimético')
            equation_text = ''
        except SyntaxError:
            equation_label.set("Erro de sintaxe")
            equation_text = ''

    def clear():
        nonlocal equation_text
        equation_text = ''
        equation_label.set('')

    root = Tk()
    root.geometry('625x700')
    root.title('Calculadora')
    root.config(bg='#555050')
    root.resizable(False, False)

    equation_label = StringVar()

    frame = Frame(root, bg='#555050')
    frame.place(x=0, y=0, width=625, height=700)

    equation = Label(frame, textvariable=equation_label, bg='black', fg='white', font=('Arial', 40))
    equation.place(x=25, y=33, width=575, height=100)

    zero_btn = Button(frame, text='0', bg='black', fg='white', font=('Arial', 40), border=0,
                      command=lambda: button_press(0))
    zero_btn.place(x=86, y=574, width=223, height=89)

    dot_btn = Button(frame, text='.', bg='black', fg='white', font=('Arial', 40), border=0,
                     command=lambda: button_press('.'))
    dot_btn.place(x=317, y=574, width=107, height=89)

    equals_btn = Button(frame, text='=', bg='#CA9100', fg='white', font=('Arial', 40), border=0, command=equals)
    equals_btn.place(x=433, y=574, width=107, height=89)

    one_btn = Button(frame, text='1', bg='black', fg='white', font=('Arial', 40), border=0,
                     command=lambda: button_press(1))
    one_btn.place(x=86, y=476, width=107, height=89)

    two_btn = Button(frame, text='2', bg='black', fg='white', font=('Arial', 40), border=0,
                     command=lambda: button_press(2))
    two_btn.place(x=204, y=476, width=107, height=89)

    three_btn = Button(frame, text='3', bg='black', fg='white', font=('Arial', 40), border=0,
                       command=lambda: button_press(3))
    three_btn.place(x=317, y=476, width=107, height=89)

    plus_btn = Button(frame, text='+', bg='#CA9100', fg='white', font=('Arial', 40), border=0,
                      command=lambda: button_press('+'))
    plus_btn.place(x=433, y=476, width=107, height=89)

    four_btn = Button(frame, text='4', bg='black', fg='white', font=('Arial', 40), border=0,
                      command=lambda: button_press(4))
    four_btn.place(x=86, y=378, width=107, height=89)

    five_btn = Button(frame, text='5', bg='black', fg='white', font=('Arial', 40), border=0,
                      command=lambda: button_press(5))
    five_btn.place(x=204, y=378, width=107, height=89)

    six_btn = Button(frame, text='6', bg='black', fg='white', font=('Arial', 40), border=0,
                     command=lambda: button_press(6))
    six_btn.place(x=317, y=378, width=107, height=89)

    minus_btn = Button(frame, text='-', bg='#CA9100', fg='white', font=('Arial', 40), border=0,
                       command=lambda: button_press('-'))
    minus_btn.place(x=433, y=378, width=107, height=89)

    seven_btn = Button(frame, text='7', bg='black', fg='white', font=('Arial', 40), border=0,
                       command=lambda: button_press(7))
    seven_btn.place(x=86, y=280, width=107, height=89)

    eight_btn = Button(frame, text='8', bg='black', fg='white', font=('Arial', 40), border=0,
                       command=lambda: button_press(8))
    eight_btn.place(x=202, y=280, width=107, height=89)

    nine_btn = Button(frame, text='9', bg='black', fg='white', font=('Arial', 40), border=0,
                      command=lambda: button_press(9))
    nine_btn.place(x=317, y=280, width=107, height=89)

    multiply_btn = Button(frame, text='*', bg='#CA9100', fg='white', font=('Arial', 40), border=0,
                          command=lambda: button_press('*'))
    multiply_btn.place(x=433, y=280, width=107, height=89)

    clear_btn = Button(frame, text='C', bg='black', fg='white', font=('Arial', 40), border=0, command=clear)
    clear_btn.place(x=86, y=182, width=223, height=89)

    modulo_btn = Button(frame, text='%', bg='black', fg='white', font=('Arial', 40), border=0,
                        command=lambda: button_press('%'))
    modulo_btn.place(x=317, y=182, width=107, height=89)

    divide_btn = Button(frame, text='/', bg='#CA9100', fg='white', font=('Arial', 40), border=0,
                        command=lambda: button_press('/'))
    divide_btn.place(x=433, y=182, width=107, height=89)

    root.mainloop()


main()
