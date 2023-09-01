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

    fundo_tela_criarconta = PhotoImage(file='imgs\\Facul-TelaInformar.png')
    label_login = Label(tela_criarconta, image=fundo_tela_criarconta)
    label_login.pack()
    
    usuarioSeek = StringVar()
    emailSeek = StringVar ()
    senhaSeek = StringVar()
    pesoSeek = IntVar()
    alturaSeek = IntVar()
    idadeSeek = IntVar()

    nome_usuario = Entry(tela_criarconta, textvariable=usuarioSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11') 
    nome_usuario.place(x=268, y=360)
    novo_email = Entry(tela_criarconta, textvariable=emailSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
    novo_email.place(x=268, y=448)
    nova_senha = Entry(tela_criarconta, textvariable=senhaSeek, width=32,bg='#dadada', borderwidth='0', font='Arial''11')
    nova_senha.place(x=268, y=538)
    peso = Entry(tela_criarconta, textvariable= pesoSeek, width=25, bg='#87e496', borderwidth='0', font='Arial''11')
    peso.place(x=730, y=358)
    altura = Entry(tela_criarconta, textvariable= alturaSeek, width=25, bg='#87e496', borderwidth='0', font='Arial''11')
    altura.place(x=730, y=445)
    idade = Entry(tela_criarconta, textvariable= idadeSeek, width=25, bg='#87e496', borderwidth='0', font='Arial''11')
    idade.place(x=730, y=536)


#função usada para cadastrar o usuario no banco de dados
    def cadastrar():
        nome_usuario = Entry(tela_criarconta, textvariable=usuarioSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11') 
        novo_email = Entry(tela_criarconta, textvariable=emailSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        nova_senha = Entry(tela_criarconta, textvariable=senhaSeek, show= "*", width=32,bg='#dadada', borderwidth='0', font='Arial''11')
        peso = Entry(tela_criarconta, textvariable= pesoSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        altura = Entry(tela_criarconta, textvariable= alturaSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        idade = Entry(tela_criarconta, textvariable= idadeSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        nome_usuario = nome_usuario.get()
        novo_email = novo_email.get()
        nova_senha = nova_senha.get()
        peso = peso.get()
        altura = altura.get()
        idade = idade.get()
 
        try: 
            #criando o banco de dados
            banco = sqlite3.connect('dados.sqlite')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, email text, senha text, peso inte, altura inte, idade inte)")
            cursor.execute("INSERT INTO usuarios (nome, email, senha, peso, altura, idade) VALUES (?, ?, ?, ?, ?, ?)", (nome_usuario, novo_email, nova_senha, peso, altura, idade))
            banco.commit()
            banco.close()
            print('Tabela cadastrada!')
            tela_criarconta.destroy()

        except sqlite3.Error as erro:
            print("Erro nos dados: ", erro)

    imgBT_criareentrar=PhotoImage(file='imgs\\bottonCriarEntrar.png')

    botao_criareentrar = Button(tela_criarconta, bd=0, image=imgBT_criareentrar, command=cadastrar)
    botao_criareentrar.place(width=135, height=43, x=512, y=589)

    tela_criarconta.mainloop()

#função usada para abrir tela principal
def abrirtela_principal():

    tela_principal= Toplevel()

    tela_principal.geometry('1280x720')
    tela_principal.resizable(False, False)
    tela_principal.title('Página Principal')
    center(tela_principal)

    email = emailSeek.get()

    fundo_tela_principal = PhotoImage(file='imgs\\Facul-TelaPrincipal.png')
    label_tela_principal = Label(tela_principal, image=fundo_tela_principal)
    label_tela_principal.pack()

    banco = sqlite3.connect('dados.sqlite')
    cursor = banco.cursor()
    cursor.execute("SELECT id, nome, altura, peso, idade FROM usuarios WHERE email = ?", (email,))
    user_info = cursor.fetchone()

    if user_info:
        id, nome, altura, peso, idade = user_info
    
    basal = (0.879 * peso) + (10.2 * altura) - (5.23 * idade) - 161

    alt_imc = altura / 100
    imc = peso / (alt_imc**2)
    if imc < 18.5:
        status_imc = Label(tela_principal, text='Abaixo do peso', bg='#008923', fg='#f2f6f4', font=("Roboto", 11))
        status_imc.place(x=95,y=293)
    elif 18.5 < imc <= 25:
        status_imc = Label(tela_principal, text='Peso ideal', bg='#008923', fg='#f2f6f4', font=("Roboto", 11))
        status_imc.place(x=95,y=293)
    elif imc <= 30:
        status_imc = Label(tela_principal, text='Sobrepeso', bg='#008923', fg='#f2f6f4', font=("Roboto", 11))
        status_imc.place(x=95,y=293)
    elif imc <= 40:
        status_imc = Label(tela_principal, text= 'Obesidade', bg='#008923', fg='#f2f6f4', font=("Roboto", 11))
        status_imc.place(x=95,y=293)
    else:
        status_imc = Label(tela_principal, text= 'Obesidade mórbida', bg='#008923', fg='#f2f6f4', font=("Roboto", 11))
        status_imc.place(x=95,y=293)

    consumo = 35 * peso
    consumo = consumo / 1000

    nome_label = Label(tela_principal, text=f"Oi, {nome}!", bg='#dadada', font=("Helvetica", 35, "bold"))
    nome_label.place(x=384, y=136) 
    basal_label = Label(tela_principal, text=f"{basal:.2f} cal.", bg='#008923', fg='#f2f6f4', font=("Roboto", 14))
    basal_label.place(x=95, y=157)  
    imc_label = Label(tela_principal, text=f"{imc:.2f} hg/m2", bg='#008923', fg='#f2f6f4', font=("Roboto", 14))
    imc_label.place(x=95, y=268)
    consumo_label = Label(tela_principal, text=f"{consumo:.2f} L", bg='#008923', fg='#f2f6f4', font=("Roboto", 14))
    consumo_label.place(x=90, y=394)

    try:
        #conferir se o usuario já é cadastrado
        cursor.execute("SELECT senha FROM usuarios WHERE email = '{}'".format(email))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    
    except:
        tela_principal.destroy()
        erro = Label(tela_login, text='Usuário não cadastrado, tente novamente!', bg= '#FAFAFA').place(x=530, y=503)

    def atualizar_informes():
    
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
        peso.place(x=465, y=336)
        altura = Entry(tela_informes, textvariable= alturaSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        altura.place(x=465, y=424)
        idade = Entry(tela_informes, textvariable= idadeSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        idade.place(x=465, y=518)

        def atualizar():

            peso = Entry(tela_informes, textvariable= pesoSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
            altura = Entry(tela_informes, textvariable= alturaSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
            idade = Entry(tela_informes, textvariable= idadeSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
            pesonovo = peso.get()
            alturanovo = altura.get()
            idadenovo = idade.get()

            try: 
                banco = sqlite3.connect('dados.sqlite')
                cursor = banco.cursor()
                cursor.execute("UPDATE usuarios SET peso=?, altura=?, idade=? WHERE id=?", (pesonovo, alturanovo, idadenovo, id))
                banco.commit()
                banco.close()
                print('Atualizado!')

            except sqlite3.Error as erro:
                print("Erro nos dados: ", erro)

        botao = Button(tela_informes, command=atualizar)
        botao.place(x=400, y=400)
    
        tela_informes.mainloop()

    fundo_botao_novasmedidas = PhotoImage(file='imgs\\medidasBotton.png')
    fundo_botao_meditacao = PhotoImage(file='imgs\\mediteBotton.png')
    fundo_botao_consumo = PhotoImage(file='imgs\\waterBotton.png')
    fundo_botao_controlepeso = PhotoImage(file='imgs\\pesoBotton.png') 

    botao_novasmedidas = Button(tela_principal, width=180, height=53, image=fundo_botao_novasmedidas, borderwidth=0, command=atualizar_informes)
    botao_novasmedidas.place(x=32, y=495)
    botao_meditacao = Button(tela_principal, width=214, height=233, image=fundo_botao_meditacao, borderwidth=0)
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

