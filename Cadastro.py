import utils
from utils import *


class Cadastro:

    def __init__(self, root):

        # mensagem de aviso
        messagebox.showinfo('Cadastro', 'Digite os dados do supervisor para validar a operação')

        self.root = root
        self.root.geometry('310x300')
        self.root.title('CADASTRO')

        # frame superior
        self.frame_cima = Frame(self.root, width=310, height=50, bg=co1, relief="flat")
        self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        self.l_cadastro = Label(self.frame_cima, text="CADASTRO", height=1, anchor=NE, font='Ivy 20 ', bg=co1, fg=co4)
        self.l_cadastro.place(x=5, y=8)

        utils.importar_imagens(self, 160, 10)

        self.l_linha = Label(self.frame_cima, width=275, text="", height=1, anchor=NW, font='Ivy 1 ', bg=co2)
        self.l_linha.place(x=10, y=45)

        # frame inferior
        self.frame_baixo = Frame(self.root, width=310, height=300, bg=co1, relief="flat")
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.l_nome_sup = Label(self.frame_baixo, text="Nome:", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4)
        self.l_nome_sup.place(x=10, y=20)
        self.nome = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1,
                          relief="solid")
        self.nome.place(x=14, y=50)

        self.l_credencial_sup = Label(self.frame_baixo, text="Crachá:", height=1, anchor=NW, font='Ivy 10 bold', bg=co1,
                                      fg=co4)
        self.l_credencial_sup.place(x=10, y=90)
        self.credencial = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.credencial.place(x=14, y=120)

        self.botao_validar = Button(self.frame_baixo, text="Validar", command=self.valida_operador, width=39, height=2,
                                    bg=co2,
                                    fg=co1, font='Ivy 8 bold',
                                    relief=RAISED, overrelief=RIDGE)
        self.botao_validar.place(x=15, y=180)

    def valida_operador(self):
        utils.get_operator(self)
        if 'ok' == utils.login(self, 2):
            self.Cadastra()

    def Cadastra(self):

        for widget in self.frame_baixo.winfo_children():
            widget.destroy()
        self.root.geometry('310x430')
        self.frame_baixo.config(height=500)

        # Dados do Operador

        self.l_nome = Label(self.frame_baixo, text="Nome:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.l_nome.place(x=10, y=20)
        self.nome = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1,
                          relief="solid")
        self.nome.place(x=14, y=50)

        self.l_credencial = Label(self.frame_baixo, text="Crachá:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                                  fg=co4)
        self.l_credencial.place(x=10, y=90)
        self.credencial = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.credencial.place(x=14, y=120)

        self.l_unidade_op = Label(self.frame_baixo, text="Unidade de operação:", height=1, anchor=NW,
                                  font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.l_unidade_op.place(x=10, y=160)
        self.unidade_op = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.unidade_op.place(x=14, y=190)

        self.l_funcao = Label(self.frame_baixo, text="Função:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                              fg=co4)
        self.l_funcao.place(x=10, y=230)
        self.funcao = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1,
                            relief="solid")
        self.funcao.place(x=14, y=260)

        self.botao_cadastrar = Button(self.frame_baixo, text="Cadastrar", command=self.inserir, width=39, height=2,
                                      bg=co2, fg=co1, font=('Ivy 8 bold'),
                                      relief=RAISED, overrelief=RIDGE)
        self.botao_cadastrar.place(x=15, y=315)

    def inserir(self):
        if self.nome.get() == "" or self.credencial.get() == "" or self.unidade_op.get() == "" or self.funcao.get() == "":
            messagebox.showerror("Erro", "Os dados não podem ser nulos!")
        else:
            list = [self.nome.get(), self.credencial.get(), self.unidade_op.get(), self.funcao.get(), 'Inativo', 'Não']
            if 'sucess' == utils.append_values(list):
                messagebox.showinfo("Sucesso!", self.funcao.get() + " adicionado!")
            else:
                messagebox.showerror("Erro", "Verifique os dados e tente novamente!")
