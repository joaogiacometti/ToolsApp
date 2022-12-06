import tkinter
from tkinter import *
from tkinter import messagebox as mb

log = False


class User:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.logged = False

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_logged(self):
        return self.logged

    def set_logged(self, boolean):
        self.logged = boolean


def main():
    root = Tk()
    root.title("Login")
    root.geometry('525x425')
    root.resizable(False, False)

    def singin():
        user = user_entry.get()
        pwd = pwd_entry.get()
        actual_user = User(user, pwd)
        if actual_user.get_user() == "admin" and actual_user.get_password() == "123":
            global log
            actual_user.set_logged(True)
            log = True
            root.destroy()
        else:
            mb.showerror(title='Erro', message='Usuário ou senha incorretos!')

    frame = Frame(root, width=525, height=425, bg='white')
    frame.place(x=0, y=0)

    heading = Label(frame, text='Login', font=('Arial', 40), fg='#61aeff', bg='white')
    heading.place(x=91, y=49)

    user_label = Label(frame, text='Usuário: ', font=('Arial', 23), fg='black', bg='white')
    user_label.place(x=91, y=134)
    user_entry = Entry(frame, font=('Arial', 23), bg='#D9D9D9', border=0)
    user_entry.place(x=237, y=134, width=224)

    pwd_label = Label(frame, text='Senha: ', font=('Arial', 23), fg='black', bg='white', padx=0, pady=0)
    pwd_label.place(x=91, y=191)
    pwd_entry = Entry(frame, width=11, font=('Arial', 23), show="*", bg='#D9D9D9', border=0)
    pwd_entry.place(x=237, y=191, width=224)
    pwd_entry.bind("<Return>", lambda e: singin())  # Faz a ação quando clicamos enter

    login_button = Button(frame, text='Entrar', bg='#61aeff', cursor='hand2', border=0, command=singin)
    login_button.place(x=156, y=276, width=212, height=49)

    register_label = Label(frame, text='Não possui uma conta?', font=('Arial', 16), fg='black', bg='white')
    register_label.place(x=112, y=377)
    register_button = Button(frame, text="Criar", bg='#61aeff', cursor='hand2', border=0)
    register_button.place(x=360, y=378, width=80)

    root.mainloop()


if __name__ == '__main__':
    main()
