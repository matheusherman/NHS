from Cadastro import Cadastro
from Formulario import Formulario
import utils
from utils import *


class Login:

    def __init__(self, root):

        self.root = root
        self.root.title('LOGIN LINHA ONLINE')

        self.frame_cima = Frame(root, width=310, height=50, bg=co1, relief="flat")
        self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        self.frame_baixo = Frame(root, width=310, height=300, bg=co1, relief="flat")
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.l_nome = Label(self.frame_cima, text="LOGIN", height=1, anchor=NE, font=('Ivy 25 '), bg=co1, fg=co4)
        self.l_nome.place(x=5, y=5)

        utils.importar_imagens(self, 160, 10)


        l_linha = Label(self.frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 1 '), bg=co2)
        l_linha.place(x=10, y=45)

        l_nome = Label(self.frame_baixo, text="Nome:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_nome.place(x=10, y=20)
        self.nome = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief="solid")
        self.nome.place(x=14, y=50)

        self.l_pass = Label(self.frame_baixo, text="Crachá:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.l_pass.place(x=10, y=90)
        self.credencial = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief="solid")
        self.credencial.place(x=14, y=120)

        botao_entrar = Button(self.frame_baixo, text="Entrar", command=self.login, width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'),
                                 relief=RAISED, overrelief=RIDGE)
        botao_entrar.place(x=15, y=180)
        botao_cadastrar = Button(self.frame_baixo, text="Cadastrar", command=self.cadastro, width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'),
                                 relief=RAISED, overrelief=RIDGE)
        botao_cadastrar.place(x=15, y=225)


    def login(self):
        utils.get_operator(self)
        if 'ok'== utils.login(self, 1):
            for widget in self.root.winfo_children():
                widget.destroy()
            Formulario(self.root)
            self.root.mainloop()


    def cadastro(self):
        Cadastro(self.root)
        self.root.mainloop()