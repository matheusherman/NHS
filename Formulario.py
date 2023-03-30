from utils import *
import utils


class Formulario:

    def __init__(self, root):
        self.root = root
        self.root.geometry('920x900')
        center(self.root)
        self.root.title('FORMULÁRIO LINHA ONLINE')

        # FRAME PRINCIPAL E BARRA DE ROLAGEM
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas, bg=co1)

        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

        # DADOS NO TOPO DA TELA

        self.frame_cima = Frame(second_frame, width=910, height=50, bg=co1, relief="flat")
        self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        l_cadastro = Label(second_frame, text="FORMULÁRIO DE INSPEÇÃO E TESTE FINAL", height=1, anchor=NE,
                           font='Ivy 25', bg=co1, fg=co4)
        l_cadastro.place(x=5, y=8)

        utils.importar_imagens(self, 730, 10)

        l_linha = Label(second_frame, width=875, text="", height=1, anchor=CENTER, font='Ivy 1 ', bg=co2)
        l_linha.place(x=10, y=45)

        # ITENS SUPERIORES

        self.frame_meio = Frame(second_frame, width=910, height=70, bg=co1, relief="flat")
        self.frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        self.l_cod_item = Label(self.frame_meio, text="Código do Item:", height=1, anchor=NW, font='Ivy 10 bold',
                                bg=co1, fg=co4)
        self.l_cod_item.place(x=10, y=20)
        self.cod_item = Entry(self.frame_meio, width=12, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.cod_item.place(x=120, y=20)

        self.l_mostra_nome = Label(self.frame_meio, text="", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4)
        self.l_mostra_nome.place(relx=0.5, y=60, anchor=CENTER)

        self.botao_checar = Button(self.frame_meio, text="Checar", command=self.testanome, width=5, height=1, bg=co2,
                                   fg=co1, font='Ivy 8 bold',
                                   relief=RAISED, overrelief=RIDGE)
        self.botao_checar.place(x=265, y=22)

        self.l_num_serie = Label(self.frame_meio, text="Número de Série:", height=1, anchor=NW, font='Ivy 10 bold',
                                 bg=co1, fg=co4)
        self.l_num_serie.place(x=330, y=20)

        self.num_serie = Entry(self.frame_meio, width=6, justify='left', font=("", 15), highlightthickness=1,
                               relief="solid")
        self.num_serie.place(x=450, y=20)

        self.l_data = Label(self.frame_meio, text="Data:", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4)
        self.l_data.place(x=600, y=20)

        self.data_atual = Label(self.frame_meio, text=datetime.now(), height=1, anchor=NW, font='Ivy 10 bold',
                                bg=co1, fg=co4)
        self.data_atual.place(x=640, y=20)

        self.frame_baixo = Frame(second_frame, width=910, height=2130, bg=co1, relief="flat")
        self.frame_baixo.grid(row=2, column=0, pady=1, padx=0, sticky=NSEW)
        self.frame_baixo.bind("<MouseWheel>", self.OnMouseWheel)

        # INSPECAO MECANICA

        self.l_linha2 = Label(self.frame_baixo, width=875, text="", height=1, anchor=CENTER, font='Ivy 1 ',
                              bg=co2).place(
            relx=0.5, y=15, anchor=CENTER)

        self.insp_mec = Label(self.frame_baixo, text="INSPEÇÃO MECÂNICA", height=1, anchor=NW, font='Ivy 15 bold',
                              bg=co1, fg="black")
        self.insp_mec.place(relx=0.5, y=15, anchor=CENTER)

        item1_1 = tkinter.StringVar()
        self.item1_1 = Checkbutton(self.frame_baixo, text="Existência de avarias no gabinete", variable=item1_1,
                                   onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1,
                                   fg=co4).place(x=10, y=20)

        item1_2 = tkinter.StringVar()
        self.item1_2 = Checkbutton(self.frame_baixo, text="Qualidade dos rodízios", variable=item1_2, onvalue="Ok", offvalue="N/A", height=1,
                                   anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=50)

        item1_3 = tkinter.StringVar()
        self.item1_3 = Checkbutton(self.frame_baixo, text="Peças soltas no interior do gabinete", variable=item1_3,onvalue="Ok", offvalue="N/A",
                                   height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=80)

        item1_4 = tkinter.StringVar()
        self.item1_4 = Checkbutton(self.frame_baixo,
                                   text="Qualidade dos botões liga/desliga, bypass, teclas de comando",
                                   variable=item1_4, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=110)

        item1_5 = tkinter.StringVar()
        self.item1_5 = Checkbutton(self.frame_baixo, text="Etiquetas, tampografia e painel", variable=item1_5, onvalue="Ok", offvalue="N/A", height=1,
                                   anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=140)

        # INSPECAO DE CABOS E CONEXÕES

        self.l_linha3 = Label(self.frame_baixo, width=875, text="", height=1, anchor=CENTER, font='Ivy 1 ',
                              bg=co2).place(
            x=10, y=170)

        self.insp_cabos = Label(self.frame_baixo, text="INSPEÇÃO DE CABOS E CONEXÕES", height=1, anchor=NW,
                                font='Ivy 15 bold', bg=co1, fg="black")
        self.insp_cabos.place(relx=0.5, y=175, anchor=CENTER)

        item2_1 = tkinter.StringVar()
        self.item2_1 = Checkbutton(self.frame_baixo,
                                   text="Verificar aperto dos parafusos das conexões das placas, disjuntores e borneiras",
                                   variable=item2_1, onvalue="Ok", offvalue="N/A", height=1, anchor=NW,
                                   font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=190)

        item2_2 = tkinter.StringVar()
        self.item2_2 = Checkbutton(self.frame_baixo, text="Modelagem dos chicotes conforme EP", variable=item2_2,
                                   onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=220)

        item2_3 = tkinter.StringVar()
        self.item2_3 = Checkbutton(self.frame_baixo, text="Qualidade das conexões faston (terminais travados) ",
                                   variable=item2_3, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=250)

        item2_4 = tkinter.StringVar()
        self.item2_4 = Checkbutton(self.frame_baixo, text="Modelagem de todosos cabos flats", variable=item2_4,
                                   onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=280)

        item2_5 = tkinter.StringVar()
        self.item2_5 = Checkbutton(self.frame_baixo, text="Solda dos cabos", variable=item2_5, onvalue="Ok", offvalue="N/A", height=1, anchor=NW,
                                   font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=310)

        item2_6 = tkinter.StringVar()
        self.item2_6 = Checkbutton(self.frame_baixo,
                                   text="Fios/chicotes prõximos aos ventiladores com risco de travamento",
                                   variable=item2_6, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=340)

        item2_7 = tkinter.StringVar()
        self.item2_7 = Checkbutton(self.frame_baixo,
                                   text="Fios ou flats cable próximos a furação da tampa ou esmagados",
                                   variable=item2_7, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=370)

        item2_8 = tkinter.StringVar()
        self.item2_8 = Checkbutton(self.frame_baixo, text="Polaridade e trava do engate rápido (se aplicável)",
                                   variable=item2_8, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=400)

        item2_9 = tkinter.StringVar()
        self.item2_9 = Checkbutton(self.frame_baixo, text="Ligação e conexão dos ventiladores/sensores/fets",
                                   variable=item2_9, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=430)

        item2_10 = tkinter.StringVar()
        self.item2_10 = Checkbutton(self.frame_baixo, text="Fixação da placa ALM_BAT no disjuntos (se aplicável) ",
                                    variable=item2_10, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=460)

        # VERIFICAÇÃO DE PLACA E COMPONENTES

        self.l_linha4 = Label(self.frame_baixo, width=875, text="", height=1, anchor=CENTER, font='Ivy 1 ',
                              bg=co2).place(
            x=10, y=500)

        self.insp_placa = Label(self.frame_baixo, text="VERIFICAÇÃO DE PLACA E COMPONENTES", height=1, anchor=NW,
                                font='Ivy 15 bold', bg=co1, fg="black")
        self.insp_placa.place(relx=0.5, y=505, anchor=CENTER)

        item3_1 = tkinter.StringVar()
        self.item3_1 = Checkbutton(self.frame_baixo, text="Fusíveis (bateria, barramento, AC e carregador)",
                                   variable=item3_1, onvalue="Ok", offvalue="N/A", height=1, anchor=NW,
                                   font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=520)

        item3_2 = tkinter.StringVar()
        self.item3_2 = Checkbutton(self.frame_baixo, text="Disjuntores", variable=item3_2, onvalue="Ok", offvalue="N/A", height=1, anchor=NW,
                                   font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=550)

        item3_3 = tkinter.StringVar()
        self.item3_3 = Checkbutton(self.frame_baixo,
                                   text="Verificar placas periféricas se não estão tortas (placa fonte, CPU, driver, etc.)",
                                   variable=item3_3, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=580)

        item3_4 = tkinter.StringVar()
        self.item3_4 = Checkbutton(self.frame_baixo, text="Verificar se existem componentes tombados (componentes PTH)",
                                   variable=item3_4, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=610)

        item3_5 = tkinter.StringVar()
        self.item3_5 = Checkbutton(self.frame_baixo,
                                   text="Medir com múltimetro o valor da resistência equivalente do inrush do barramento",
                                   variable=item3_5, onvalue="Ok", offvalue="N/A", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4).place(
            x=10, y=640)

        # ENSAIOS CONFORME PARÂMETROS DE TESTE

        l_linha6 = Label(self.frame_baixo, width=875, text="", height=1, anchor=S, font='Ivy 1 ', bg=co2).place(
            relx=0.5, y=685, anchor=CENTER)

        ensaio = Label(self.frame_baixo, text="ENSAIOS CONFORME PARÂMETROS DE TESTE", height=1, anchor=NW,
                       font='Ivy 15 bold',
                       bg=co1, fg="black")
        ensaio.place(relx=0.5, y=685, anchor=CENTER)

        item4_1 = tkinter.StringVar()
        self.item4_1 = Checkbutton(self.frame_baixo,
                                   text="Comunicação (gravação cartão SD, data/hora, crachá, valores, ...)OK",
                                   variable=item4_1, onvalue="Ok", offvalue="N/A", height=1, anchor=NW,
                                   font='Ivy 10 bold', bg=co1, fg=co4).place(x=10, y=705)

        l_item4_2 = Label(self.frame_baixo, text="Calibração Vout no inversor", height=1, anchor=NW,
                          font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_2.place(x=10, y=735)
        self.item4_2 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_2.place(relx=0.75, y=735)

        self.var4_2 = StringVar()
        utils.combobox(self, 0.82, 738, self.var4_2, volts)

        l_item4_3 = Label(self.frame_baixo, text="Calibração Vout no display (se aplicável)", height=1, anchor=NW,
                          font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_3.place(x=10, y=765)
        self.item4_3 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_3.place(relx=0.75, y=765)

        self.var4_3 = StringVar()
        utils.combobox(self, 0.82, 768, self.var4_3, volts)

        l_item4_4 = Label(self.frame_baixo, text="Largura Flybacks", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                          fg=co4)
        l_item4_4.place(x=10, y=795)
        self.item4_4 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_4.place(relx=0.75, y=795)

        self.var4_4 = StringVar()
        utils.combobox(self, 0.82, 798, self.var4_4, volts)

        l_item4_5 = Label(self.frame_baixo, text="Polaridade Flybacks", height=1, anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item4_5.place(x=10, y=825)
        self.item4_5 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_5.place(relx=0.75, y=825)

        self.var4_5 = StringVar()
        utils.combobox(self, 0.82, 828, self.var4_5, volts)

        l_item4_6 = Label(self.frame_baixo,
                          text="Tensão máxima no FET da fonte na partida e plena carga (Overshut)(Bateria deve estar carregada)",
                          height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_6.place(x=10, y=855)
        self.item4_6 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_6.place(relx=0.75, y=855)

        self.var4_6 = StringVar()
        utils.combobox(self, 0.82, 858, self.var4_6, volts)

        l_item4_7 = Label(self.frame_baixo, text="+5V fonte principal", height=1, anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item4_7.place(x=10, y=885)
        self.item4_7 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_7.place(relx=0.75, y=885)

        self.var4_7 = StringVar()
        utils.combobox(self, 0.82, 888, self.var4_7, volts)

        l_item4_8 = Label(self.frame_baixo, text="+12V fonte principal", height=1, anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item4_8.place(x=10, y=915)

        l_item4_8_1 = Label(self.frame_baixo, text="Rede:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_8_1.place(relx=0.17, y=915)
        self.item4_8_1 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                               relief="solid")
        self.item4_8_1.place(relx=0.22, y=915)

        self.var4_8_1 = StringVar()
        utils.combobox(self, 0.29, 918, self.var4_8_1, volts)

        l_item4_8_2 = Label(self.frame_baixo, text="Bateria baixa:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                            fg=co4)
        l_item4_8_2.place(relx=0.35, y=915)
        self.item4_8_2 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                               relief="solid")
        self.item4_8_2.place(relx=0.46, y=915)

        self.var4_8_2 = StringVar()
        utils.combobox(self, 0.53, 918, self.var4_8_2, volts)

        l_item4_8_3 = Label(self.frame_baixo, text="Plena carga:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                            fg=co4)
        l_item4_8_3.place(relx=0.585, y=915)
        self.item4_8_3 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                               relief="solid")
        self.item4_8_3.place(relx=0.68, y=915)

        self.var4_8_3 = StringVar()
        utils.combobox(self, 0.75, 918, self.var4_8_3, volts)

        l_item4_8_4 = Label(self.frame_baixo, text="Vazio:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_8_4.place(relx=0.81, y=915)
        self.item4_8_4 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                               relief="solid")
        self.item4_8_4.place(relx=0.86, y=915)

        self.var4_8_4 = StringVar()
        utils.combobox(self, 0.93, 918, self.var4_8_4, volts)

        l_item4_9 = Label(self.frame_baixo, text="+24V fonte principal", height=1, anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item4_9.place(x=10, y=945)
        self.item4_9 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item4_9.place(relx=0.75, y=945)

        self.var4_9 = StringVar()
        utils.combobox(self, 0.82, 948, self.var4_9, volts)

        l_item4_10 = Label(self.frame_baixo, text="+5V regulado fonte principal", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_10.place(x=10, y=975)
        self.item4_10 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_10.place(relx=0.75, y=975)

        self.var4_10 = StringVar()
        utils.combobox(self, 0.82, 978, self.var4_10, volts)

        l_item4_11 = Label(self.frame_baixo, text="+3V3 fonte principal", height=1, anchor=NW, font=('Ivy 10 bold'),
                           bg=co1, fg=co4)
        l_item4_11.place(x=10, y=1005)
        self.item4_11 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_11.place(relx=0.75, y=1005)

        self.var4_11 = StringVar()
        utils.combobox(self, 0.82, 1008, self.var4_11, volts)

        l_item4_12 = Label(self.frame_baixo, text="+12V_B da fonte principal (isolado)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_12.place(x=10, y=1035)
        self.item4_12 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_12.place(relx=0.75, y=1035)

        self.var4_12 = StringVar()
        utils.combobox(self, 0.82, 1038, self.var4_12, volts)

        l_item4_13 = Label(self.frame_baixo, text="+24V_B da fonte principal (isolado)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_13.place(x=10, y=1065)
        self.item4_13 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_13.place(relx=0.75, y=1065)

        self.var4_13 = StringVar()
        utils.combobox(self, 0.82, 1068, self.var4_13, volts)

        l_item4_14 = Label(self.frame_baixo, text="+1,65V", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_14.place(x=10, y=1095)
        self.item4_14 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_14.place(relx=0.75, y=1095)

        self.var4_14 = StringVar()
        utils.combobox(self, 0.82, 1098, self.var4_14, volts)

        l_item4_15 = Label(self.frame_baixo, text="Vsub(in) em 120V", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                           fg=co4)
        l_item4_15.place(x=10, y=1125)
        self.item4_15 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_15.place(relx=0.75, y=1125)

        self.var4_15 = StringVar()
        utils.combobox(self, 0.82, 1128, self.var4_15, volts)

        l_item4_16 = Label(self.frame_baixo, text="Vsob(in) em 120V", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                           fg=co4)
        l_item4_16.place(x=10, y=1155)
        self.item4_16 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_16.place(relx=0.75, y=1155)

        self.var4_16 = StringVar()
        utils.combobox(self, 0.82, 1158, self.var4_16, volts)

        l_item4_17 = Label(self.frame_baixo, text="Vsub(in) em 220V", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                           fg=co4)
        l_item4_17.place(x=10, y=1185)
        self.item4_17 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_17.place(relx=0.75, y=1185)

        self.var4_17 = StringVar()
        utils.combobox(self, 0.82, 1188, self.var4_17, volts)

        l_item4_18 = Label(self.frame_baixo, text="Vsob(in) em 220V", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                           fg=co4)
        l_item4_18.place(x=10, y=1215)
        self.item4_18 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_18.place(relx=0.75, y=1215)

        self.var4_18 = StringVar()
        utils.combobox(self, 0.82, 1218, self.var4_18, volts)

        l_item4_19 = Label(self.frame_baixo, text="Vout (trifásico por fase)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_19.place(x=10, y=1255)

        l_item4_19_1 = Label(self.frame_baixo, text="A:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_19_1.place(relx=0.23, y=1255)
        self.item4_19_1 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.item4_19_1.place(relx=0.25, y=1255)

        self.var4_19_1 = StringVar()
        utils.combobox(self, 0.32, 1258, self.var4_19_1, volts)

        l_item4_19_2 = Label(self.frame_baixo, text="B:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_19_2.place(relx=0.43, y=1255)
        self.item4_19_2 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.item4_19_2.place(relx=0.45, y=1255)

        self.var4_19_2 = StringVar()
        utils.combobox(self, 0.52, 1258, self.var4_19_2, volts)

        l_item4_19_3 = Label(self.frame_baixo, text="C:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_19_3.place(relx=0.63, y=1255)
        self.item4_19_3 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.item4_19_3.place(relx=0.65, y=1255)

        self.var4_19_3 = StringVar()
        utils.combobox(self, 0.72, 1258, self.var4_19_3, volts)

        l_item4_20 = Label(self.frame_baixo, text="V de flutuação da bateria", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_20.place(x=10, y=1295)
        self.item4_20 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_20.place(relx=0.75, y=1295)

        self.var4_20 = StringVar()
        utils.combobox(self, 0.82, 1298, self.var4_20, volts)

        l_item4_21 = Label(self.frame_baixo, text="V de desligamento da bateria", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_21.place(x=10, y=1325)
        self.item4_21 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_21.place(relx=0.75, y=1325)

        self.var4_21 = StringVar()
        utils.combobox(self, 0.82, 1328, self.var4_21, volts)

        l_item4_22 = Label(self.frame_baixo, text="Corrente em vazio da bateria", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_22.place(x=10, y=1355)
        self.item4_22 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_22.place(relx=0.75, y=1355)

        self.var4_22 = StringVar()
        utils.combobox(self, 0.82, 1358, self.var4_22, amps)

        l_item4_23 = Label(self.frame_baixo, text="Tensão positiva no gate da chave (todas)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_23.place(x=10, y=1385)
        self.item4_23 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_23.place(relx=0.75, y=1385)

        self.var4_23 = StringVar()
        utils.combobox(self, 0.82, 1388, self.var4_23, volts)

        l_item4_24 = Label(self.frame_baixo, text="Tensão negativa no gate da chave (todas)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_24.place(x=10, y=1415)
        self.item4_24 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_24.place(relx=0.75, y=1415)

        self.var4_2 = StringVar()
        utils.combobox(self, 0.82, 1418, self.var4_2, volts)

        l_item4_25 = Label(self.frame_baixo, text="Tensão do barramento", height=1, anchor=NW, font=('Ivy 10 bold'),
                           bg=co1, fg=co4)
        l_item4_25.place(x=10, y=1445)
        self.item4_25 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_25.place(relx=0.75, y=1445)

        self.var4_25 = StringVar()
        utils.combobox(self, 0.82, 1448, self.var4_25, volts)

        l_item4_26 = Label(self.frame_baixo, text="Potência excessiva por fase (Trifásico)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_26.place(x=10, y=1445)

        l_item4_26_1 = Label(self.frame_baixo, text="A:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_26_1.place(relx=0.33, y=1448)
        self.item4_26_1 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.item4_26_1.place(relx=0.35, y=1445)

        self.var4_26_1 = StringVar()
        utils.combobox(self, 0.42, 1448, self.var4_26_1, watts)

        l_item4_26_2 = Label(self.frame_baixo, text="B:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_26_2.place(relx=0.53, y=1448)
        self.item4_26_2 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.item4_26_2.place(relx=0.55, y=1444)

        self.var4_26_2 = StringVar()
        utils.combobox(self, 0.62, 1448, self.var4_26_2, watts)

        l_item4_26_3 = Label(self.frame_baixo, text="C:", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_26_3.place(relx=0.73, y=1448)
        self.item4_26_3 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                                relief="solid")
        self.item4_26_3.place(relx=0.75, y=1444)

        self.var4_26_3 = StringVar()
        utils.combobox(self, 0.82, 1448, self.var4_26_3, watts)

        l_item4_27 = Label(self.frame_baixo, text="Potência excessiva total", height=1, anchor=NW, font=('Ivy 10 bold'),
                           bg=co1, fg=co4)
        l_item4_27.place(x=10, y=1475)
        self.item4_27 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_27.place(relx=0.75, y=1475)

        self.var4_27 = StringVar()
        utils.combobox(self, 0.82, 1478, self.var4_27, watts)

        l_item4_28 = Label(self.frame_baixo, text="Corrente de curto circuito (proteção hardware)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_28.place(x=10, y=1505)
        self.item4_28 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_28.place(relx=0.75, y=1505)

        self.var4_28 = StringVar()
        utils.combobox(self, 0.82, 1508, self.var4_28, amps)

        l_item4_29 = Label(self.frame_baixo, text="Corrente de curto circuito (proteção firmware)", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_29.place(x=10, y=1535)
        self.item4_29 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_29.place(relx=0.75, y=1535)

        self.var4_29 = StringVar()
        utils.combobox(self, 0.82, 1538, self.var4_29, amps)

        l_item4_30 = Label(self.frame_baixo, text="Detecção de faut e tempo da proteção", height=1, anchor=NW,
                           font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_30.place(x=10, y=1565)
        self.item4_30 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_30.place(relx=0.75, y=1565)

        self.var4_30 = StringVar()
        utils.combobox(self, 0.82, 1568, self.var4_30, volts)

        l_item4_31 = Label(self.frame_baixo, text="Corrente do carregador", height=1, anchor=NW, font=('Ivy 10 bold'),
                           bg=co1, fg=co4)
        l_item4_31.place(x=10, y=1595)
        self.item4_31 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_31.place(relx=0.75, y=1595)

        self.var4_31 = StringVar()
        utils.combobox(self, 0.82, 1598, self.var4_31, amps)

        l_item4_32 = Label(self.frame_baixo, text="Autonomia com carga nominal (modelos com bateria interna)", height=1,
                           anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item4_32.place(x=10, y=1625)
        self.item4_32 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                              relief="solid")
        self.item4_32.place(relx=0.75, y=1625)

        self.var4_32 = StringVar()
        utils.combobox(self, 0.82, 1628, self.var4_32, volts)

        # INSPECAO TERMICA

        l_linha8 = Label(self.frame_baixo, width=875, text="", height=1, anchor=S, font='Ivy 1 ', bg=co2).place(
            relx=0.5, y=1675, anchor=CENTER)

        termica = Label(self.frame_baixo, text="INSPEÇÃO TÉRMICA", height=1, anchor=NW,
                        font='Ivy 15 bold',
                        bg=co1, fg="black")
        termica.place(relx=0.5, y=1675, anchor=CENTER)

        l_item5_1 = Label(self.frame_baixo, text="Indutores (com carga nominal)", height=1, anchor=NW,
                          font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item5_1.place(x=10, y=1705)
        self.item5_1 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_1.place(relx=0.75, y=1705)

        self.var5_1 = StringVar()
        utils.combobox(self, 0.82, 1708, self.var5_1, degrees)

        l_item5_2 = Label(self.frame_baixo, text="Transformador com carga nominal não linear (se aplicável)", height=1,
                          anchor=NW,
                          font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item5_2.place(x=10, y=1735)
        self.item5_2 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_2.place(relx=0.75, y=1735)

        self.var5_2 = StringVar()
        utils.combobox(self, 0.82, 1738, self.var5_2, degrees)

        l_item5_3 = Label(self.frame_baixo,
                          text="Snubber e grampeadores (com ventiladores a 100% e bateria carregando - indicar posição)",
                          height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,
                          fg=co4)
        l_item5_3.place(x=10, y=1765)
        self.item5_3 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_3.place(relx=0.75, y=1765)

        self.var5_3 = StringVar()
        utils.combobox(self, 0.82, 1768, self.var5_3, degrees)

        l_item5_4 = Label(self.frame_baixo, text="Diodos fonte (com ventiladores a 100% e carga nominal)", height=1,
                          anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item5_4.place(x=10, y=1795)
        self.item5_4 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_4.place(relx=0.75, y=1795)

        self.var5_4 = StringVar()
        utils.combobox(self, 0.82, 1798, self.var5_4, degrees)

        l_item5_5 = Label(self.frame_baixo, text="Etapa de potência e fusíveis (com carga nominal)", height=1,
                          anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item5_5.place(x=10, y=1825)
        self.item5_5 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_5.place(relx=0.75, y=1825)

        self.var5_5 = StringVar()
        utils.combobox(self, 0.82, 1828, self.var5_5, degrees)

        l_item5_6 = Label(self.frame_baixo,
                          text="Trafinho do carregador (com bateria carregando)",
                          height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        l_item5_6.place(x=10, y=1855)
        self.item5_6 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_6.place(relx=0.75, y=1855)

        self.var5_6 = StringVar()
        utils.combobox(self, 0.82, 1858, self.var5_6, degrees)

        l_item5_7 = Label(self.frame_baixo, text="IGBT do carregador (com bateria carregando)", height=1, anchor=NW,
                          font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item5_7.place(x=10, y=1885)
        self.item5_7 = Entry(self.frame_baixo, width=5, justify='left', font=("", 15), highlightthickness=1,
                             relief="solid")
        self.item5_7.place(relx=0.75, y=1885)

        self.var5_7 = StringVar()
        utils.combobox(self, 0.82, 1888, self.var5_7, degrees)

        l_item5_8 = Label(self.frame_baixo,
                          text="Identificar todos componentes com temperatura superior a 80°C que não constam nos itens listados acima",
                          height=1, anchor=NW, font=('Ivy 10 bold'),
                          bg=co1, fg=co4)
        l_item5_8.place(x=10, y=1915)
        self.item5_8 = Text(self.frame_baixo, width=80, height=5, font=("", 15), highlightthickness=1,
                            relief="solid")
        self.item5_8.place(x=10, y=1935)

        self.botao_validar = Button(self.frame_baixo, text="Enviar", command=self.envio, width=39, height=2,
                                    bg=co6, fg=co1, font='Ivy 8 bold', relief=RAISED, overrelief=RIDGE)
        self.botao_validar.place(relx=0.5, anchor=CENTER, y=2100)

    def testanome(self):
        if 1 != utils.get_equip_name(self):
            messagebox.showwarning("Erro", "Produto não encontrado, verifique o código do equipamento!")

    def envio(self):
        utils.save_form(self)

    def OnMouseWheel(self, event):
        self.my_scrollbar.yview("scroll", event.delta, "units")
        return "break"

