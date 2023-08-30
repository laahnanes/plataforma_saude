from tkinter import * 
import sqlite3

tela_login = Tk()

#função usada para centralizar as telas
def center(win):
    
    win.update_idletasks()  
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry(f'{width}x{height}+{x}+{y}')

#função para abrir a tela criar conta
def abrirtela_criarconta():
    
    tela_criarconta= Toplevel()
    tela_criarconta.geometry('1280x720')
    tela_criarconta.resizable(False, False)
    tela_criarconta.title('Heath Point')
    center(tela_criarconta)

    fundo_tela_criarconta = PhotoImage(file='imgs\\criar.png')
    label_login = Label(tela_criarconta, image=fundo_tela_criarconta)
    label_login.pack()
    
    usuarioSeek = StringVar()
    emailSeek = StringVar ()
    senhaSeek = StringVar()

    nome_usuario = Entry(tela_criarconta, textvariable=usuarioSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11') 
    nome_usuario.place(x=465, y=336)
    novo_email = Entry(tela_criarconta, textvariable=emailSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
    novo_email.place(x=465, y=424)
    nova_senha = Entry(tela_criarconta, textvariable=senhaSeek, width=32,bg='#dadada', borderwidth='0', font='Arial''11')
    nova_senha.place(x=465, y=518)

#função usada para cadastrar o usuario no banco de dados
    def cadastrar():
        nome_usuario = Entry(tela_criarconta, textvariable=usuarioSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11') 
        novo_email = Entry(tela_criarconta, textvariable=emailSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        nova_senha = Entry(tela_criarconta, textvariable=senhaSeek, show= "*", width=32,bg='#dadada', borderwidth='0', font='Arial''11')
        nome_usuario = nome_usuario.get()
        novo_email = novo_email.get()
        nova_senha = nova_senha.get()
 
        try: 
            #criando o banco de dados
            banco = sqlite3.connect('dados.sqlite')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, email text, senha text)")
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome_usuario, novo_email, nova_senha))
            banco.commit()
            banco.close()
            print('Tabela cadastrada!')
            tela_criarconta.destroy()

        except sqlite3.Error as erro:
            print("Erro nos dados: ", erro)

    imgBT_criareentrar=PhotoImage(file='imgs\\bottonCriarEntrar.png')

    botao_criareentrar = Button(tela_criarconta, bd=0, image=imgBT_criareentrar, command=cadastrar)
    botao_criareentrar.place(width=135, height=43, x=571, y=572)

    tela_criarconta.mainloop()

#função usada para abrir tela principal
def abrirtela_principal():

    tela_principal= Toplevel()

    tela_principal.geometry('1280x720')
    tela_principal.resizable(False, False)
    tela_principal.title('Página Principal')
    center(tela_principal)

    email = emailSeek.get()

    fundo_tela_principal = PhotoImage(file='imgs\\TelaPrincipal.png')
    label_tela_principal = Label(tela_principal, image=fundo_tela_principal)
    label_tela_principal.pack()

    banco = sqlite3.connect('dados.sqlite')
    cursor = banco.cursor()
    try:
        #conferir se o usuario já é cadastrado
        cursor.execute("SELECT senha FROM usuarios WHERE email = '{}'".format(email))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    
    except:
        tela_principal.destroy()
        erro = Label(tela_login, text='Usuário não cadastrado, tente novamente!', bg= '#FAFAFA').place(x=530, y=503)

    def abrirtela_informes():
    
        tela_informes = Toplevel()
        tela_informes.geometry('1280x720')
        tela_informes.resizable(False, False)
        tela_informes.title('Heath Point')
        center(tela_informes)

        fundo_tela_informes = PhotoImage(file='imgs\\infor.png')
        label_informes = Label(tela_informes, image=fundo_tela_informes)
        label_informes.pack()

        pesoSeek = IntVar()
        alturaSeek = IntVar()
        idadeSeek = IntVar()

        peso = Entry(tela_informes, textvariable= pesoSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        peso.place(x=470, y=339)
        altura = Entry(tela_informes, textvariable= alturaSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        altura.place(x=470, y=425)
        idade = Entry(tela_informes, textvariable= idadeSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        idade.place(x=470, y=516)

        def atualizar():

            peso = Entry(tela_informes, textvariable= pesoSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
            altura = Entry(tela_informes, textvariable= alturaSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
            idade = Entry(tela_informes, textvariable= idadeSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
            peso = peso.get()
            altura = altura.get()
            idade = idade.get()

            try: 
                banco = sqlite3.connect('dados.sqlite')
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS medidas (id INTEGER PRIMARY KEY AUTOINCREMENT, peso inte, altura inte, idade inte)")
                cursor.execute("INSERT INTO medidas (peso, altura, idade) VALUES (?, ?, ?)", (peso, altura, idade))
                banco.commit()
                banco.close()
                print('Tabela cadastrada!')

            except sqlite3.Error as erro:
                print("Erro nos dados: ", erro)

        botao = Button(tela_informes, command=atualizar)
        botao.place(x=400, y=400)
    
        tela_informes.mainloop()

    fundo_botao_novasmedidas = PhotoImage(file='imgs\\medidasBotton.png')
    fundo_botao_meditacao = PhotoImage(file='imgs\\mediteBotton.png')
    fundo_botao_consumo = PhotoImage(file='imgs\\waterBotton.png')
    fundo_botao_controlepeso = PhotoImage(file='imgs\\pesoBotton.png') 

    botao_novasmedidas = Button(tela_principal, width=180, height=53, image=fundo_botao_novasmedidas, borderwidth=0, command=abrirtela_informes )
    botao_novasmedidas.place(x=32, y=495)
    botao_meditacao = Button(tela_principal, width=214, height=233, image=fundo_botao_meditacao, borderwidth=0, command=tmb)
    botao_meditacao.place(x=348, y=385)
    botao_consumo = Button(tela_principal, width=214, height=233, image=fundo_botao_consumo, borderwidth=0)
    botao_consumo.place(x=660, y=385)
    botao_controlepeso = Button(tela_principal, width=214, height=233, image=fundo_botao_controlepeso, borderwidth=0)
    botao_controlepeso.place(x=969, y=385)

    tela_principal.mainloop()

#conteúdo primeira tela

tela_login.geometry('1280x720')
tela_login.resizable(False, False)
tela_login.title('Heath Point')
tela_login.iconbitmap(default='imgs\\appi.ico')
center(tela_login)

fundo_tela_login = PhotoImage(file='imgs\\login.png')
Label_login = Label(tela_login, image=fundo_tela_login).pack()

senhaSeek = StringVar()
emailSeek = StringVar()

email = Entry(tela_login, textvariable=emailSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11').place(x=465, y=360)
senha = Entry(tela_login, textvariable=senhaSeek, show= "*", width=32,bg='#dadada', borderwidth='0', font='Arial''11').place(x=465, y=464)

imgBT_criarconta=PhotoImage(file='imgs\\bottonCriar.png')
imgBT_entrar=PhotoImage(file='imgs\\bottonEntrar.png')

botao_criarconta=Button(tela_login, bd=0, image=imgBT_criarconta, command= abrirtela_criarconta)
botao_criarconta.place(width=135, height=43, x=652, y=536)

botao_entrar=Button(tela_login, bd=0, image=imgBT_entrar, command=abrirtela_principal)
botao_entrar.place(width=135, height=43, x=490, y=536)

tela_login.mainloop()

