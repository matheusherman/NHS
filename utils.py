import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import csv
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
import boto3

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = '#172953'  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#8B0000"  # vermelho
co6 = '#009900'  # verde

volts = ['V', 'mV', 'μV', 'nV']
amps = ['A', 'mA', 'μA', 'nA']
watts = ['kW', 'W', 'mW', 'μW']
degrees = ['°C']

cabecalho = ['sn', 'date', 'max_volt', 'volt_limit', 'grid', 'low_bat', 'full_load', 'low_tole', 'upp_tole', 'empty',
             'main_source', 'low_tole_B', 'upp_tole_B', 'emp_curr_bat', 'emp_max_curr', 'hard_protec', 'cb_limit_hard',
             'firm_protec', 'cb_limit_firm', 'char_curr', 'max_char_curr', 'min_char_curr', 'induc', 'max_temp_induc',
             'trans_non_lin_char', 'max_temp_char', 'snb', 'res_temp_limit', 'stp', 'diode_temp', 'diode_temp_limit',
             'pot', 'max_IGBT_fuse_temp', 'fuse', 'char_IGBT', 'max_IGBT_temp']

def cred():
    path = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', path)
        return creds
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', path)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


def get_operator(self):
    file_ID = '1tZv8tehSzgz16hpq5TTlxdlk4vlcsFxvGmMIE2dvVPc'
    file_NAME = 'Listagem dos Colaboradores'

    try:
        service = build('sheets', 'v4', credentials=cred())
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=file_ID,
                                    range=file_NAME).execute()
        self.values = result.get('values', [])
        return self.values
    except HttpError as error:
        messagebox.showerror("Erro", error)


def append_values(list):
    file_ID = '1tZv8tehSzgz16hpq5TTlxdlk4vlcsFxvGmMIE2dvVPc'
    file_NAME = 'Listagem dos Colaboradores'

    try:
        service = build('sheets', 'v4', credentials=cred())
        values = [list, ]
        body = {'values': values}
        result = service.spreadsheets().values().append(spreadsheetId=file_ID, range=file_NAME, valueInputOption="RAW",
                                                        body=body).execute()
        return 'sucess'
    except HttpError as error:
        messagebox.showerror("Erro", error)


def get_equip_name(self):
    file_ID = '1UUO2-XjsoQFSVSy3mxhN1u0dKwC5mjHmvs0FiQvBVmU'
    file_NAME = 'Códigos e descrições - Modelos NHS onlines'

    try:
        service = build('sheets', 'v4', credentials=cred())
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=file_ID,
                                    range=file_NAME).execute()
        values = result.get('values', [])

        if not values:
            messagebox.showinfo("Planilha vazia",'Dados não encontrados')
            return

        for linhas in values:
            cod_equip = linhas[0]
            nome_equip = linhas[1]
            if cod_equip.lower() == self.cod_item.get().lower():
                self.l_mostra_nome.configure(text=nome_equip)
                return 1
    except HttpError as error:
        messagebox.showerror("Erro", error)


def get_equip_code(self):
    file_ID = '1UUO2-XjsoQFSVSy3mxhN1u0dKwC5mjHmvs0FiQvBVmU'
    file_NAME = 'Códigos e descrições - Modelos NHS onlines'

    try:
        service = build('sheets', 'v4', credentials=cred())
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=file_ID,
                                    range=file_NAME).execute()
        values = result.get('values', [])

        if not values:
            messagebox.showinfo("Planilha vazia",'Dados não encontrados')
            return

        for linhas in values:
            cod_equip = linhas[0]
            if cod_equip.lower() == self.cod_item.get().lower():
                return 1

    except HttpError as error:
        messagebox.showerror("Erro", error)


def login(self, num):
    check = 1
    if num == 1:
        for linhas in self.values:
            try:
                nome_colab = linhas[0]
                cracha_colab = linhas[1]
                if self.nome.get() == nome_colab and self.credencial.get() == cracha_colab:
                    check = 0
            except:
                messagebox.showerror('Erro', 'Erro')

        if 0 == check:
            messagebox.showinfo('Login', ' Seja bem vindo de volta ' + self.nome.get())
            return 'ok'
        else:
            messagebox.showwarning('Erro', 'Verifique o nome ou a crendencial')
    elif num == 2:
        for linhas in self.values:
            try:
                nome_colab = linhas[0]
                cracha_colab = linhas[1]
                funcao = linhas[3]
                if self.nome.get() == nome_colab and self.credencial.get() == cracha_colab and (
                        funcao == 'Supervisor' or 'Gerente de Projeto'):
                    return 'ok'
            except:
                messagebox.showerror('Erro', 'Erro')

        if 0 == check:
            messagebox.showinfo('Cadastro', 'Operador encontrado! \n Insira as informações!')
            for widget in self.frame_baixo.winfo_children():
                widget.destroy()
            return
        else:
            messagebox.showwarning('Erro', 'Verifique o nome ou a crendencial')


def combobox(self, posx, posy, var, values):
    cb = ttk.Combobox(self.frame_baixo, textvariable=var, values=values, width=3)
    cb.current(0)
    cb['state'] = ['readonly']
    cb.place(relx=posx, y=posy)


def importar_imagens(self, posx, posy):
    imgNHS = Image.open("NHS.png")
    NHS_rez = imgNHS.resize((140, 30))
    imgNHS = ImageTk.PhotoImage(NHS_rez)
    Label_imageNHS = Label(self.frame_cima, image=imgNHS, bg=co1)
    Label_imageNHS.place(x=posx, y=posy)
    Label_imageNHS.image = imgNHS


def center(win):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()

path = ""

def save_form(self):
    arquivo = self.cod_item.get().upper()
    data = datetime.now()
    nome_final = f"td-online-{arquivo}-{data.strftime('%Y')}-{data.strftime('%m')}-{data.strftime('%d')}"

    global path
    if path == "":
        path = askdirectory()

    if get_equip_code(self) != 1:
        messagebox.showwarning("Erro", "Produto não encontrado, verifique o código do equipamento!")
    elif self.num_serie.get() == "":
        messagebox.showwarning("Erro", "Digite o número de série!")
    else:
        try:
            if os.path.exists(f"{path}/{nome_final}.csv"):
                with open(f"{path}/{nome_final}.csv", 'a', newline='', encoding='utf-8') as file:
                    csv.writer(file, delimiter=',').writerow(
                        [self.num_serie.get(), data, self.item4_6.get(), '750', self.item4_8_1.get(), self.item4_8_2.get(),
                         self.item4_8_3.get(), '12', '13', self.item4_8_4.get(), self.item4_12.get(), '12', '14',
                         self.item4_22.get(), '1000', self.item4_28.get(), '100', self.item4_29.get(), '100',
                         self.item4_31.get(), '1000', '500', self.item5_1.get(), '100', self.item5_2.get(), '100',
                         self.item5_3.get(), '80', self.item5_3.get(), self.item5_4.get(), '80', self.item5_4.get(), '80',
                         self.item5_5.get(), '80', self.item5_5.get(), self.item5_7.get(), '80'])
            else:
                with open(f"{path}/{nome_final}.csv", 'w', newline='', encoding='utf-8') as file:
                    csv.writer(file, delimiter=',').writerow(cabecalho) #cabecalho
                    csv.writer(file, delimiter=',').writerow( #unidades
                        ['', '', self.var4_6.get(), 'V', self.var4_8_1.get(), self.var4_8_2.get(), self.var4_8_3.get(), 'V',
                         'V', self.var4_8_4.get(), self.var4_12.get(), 'V', 'V', self.var4_22.get(), 'mA',
                         self.var4_28.get(),
                         'A', self.var4_29.get(), 'A', self.var4_31.get(), 'mA', 'mA', self.var5_1.get(), '&#xBAC',
                         self.var5_2.get(), '°C', self.var5_3.get(), '°C', self.var5_3.get(), self.var5_4.get(), '°C',
                         self.var5_4.get(), '°C', self.var5_5.get(), '°C', self.var5_5.get(), self.var5_7.get(), '°C'])
                    csv.writer(file, delimiter=',').writerow( #dados
                        [self.num_serie.get(), data, self.item4_6.get(), '750', self.item4_8_1.get(), self.item4_8_2.get(),
                         self.item4_8_3.get(), '12', '13', self.item4_8_4.get(), self.item4_12.get(), '12', '14',
                         self.item4_22.get(), '1000', self.item4_28.get(), '100', self.item4_29.get(), '100',
                         self.item4_31.get(), '1000', '500', self.item5_1.get(), '100', self.item5_2.get(), '100',
                         self.item5_3.get(), '80', self.item5_3.get(), self.item5_4.get(), '80', self.item5_4.get(), '80',
                         self.item5_5.get(), '80', self.item5_5.get(), self.item5_7.get(), '80'])
            data_lake_insert(self, nome_final, path)
            messagebox.showinfo("Sucesso", "Dados Salvos!")
        except PermissionError:
            messagebox.showerror("Permissão Negada", "Feche o arquivo e tente novamente!")
        except Exception as e:
            messagebox.showerror("Erro", e)


def data_lake_insert(self, nome_final, path):
    date = datetime.now()
    s3_client = boto3.client(
        's3',
        aws_access_key_id='AKIAXTE5DZMDJAK4NVHZ',
        aws_secret_access_key='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'
    )

    s3_client.upload_file(
        Filename=f'{path}/{nome_final}.csv',
        Bucket='datalake-dev-landing',
        Key=f"efd/testing-data/line=online/sn={self.cod_item.get().upper()}/year={date.strftime('%Y')}/month={date.strftime('%m')}/day={date.strftime('%d')}/{nome_final}.csv"
    )