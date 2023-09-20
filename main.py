from tkinter import * 
import sqlite3
import datetime
import matplotlib.pyplot as plt

tela_login = Tk()

#função usada para centralizar as telas (Pedro)
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

#função do cronômetro (Pedro)

def abrir_meditacao():

    # cores
    cor1 = "#FFFFFF"  # white / branco
    cor2 = "#21c25c"  # green / verde Botão
    cor3 = "#21c25c"  # green / verde Contador

    #janela
    janela = Tk()
    janela.title('Meditação')
    janela.geometry('300x180')
    janela.configure(bg=cor1)
    janela.wm_resizable(width=False, height=False)

    #Definindo variaveis globais

    global tempo
    global radar
    global contador
    global limitador

    limitador = 58
    tempo = '00:00:00'
    rodar = True
    contador = -3

    #funcao iniciar
    def iniciar():
        global tempo
        global contador
        global limitador

        if rodar:
            #Antes do cronômetro começar
            if contador <= -1:
                inicio = 'Comecando em' +str(contador)
                Label_tempo['text'] = inicio
                Label_tempo['font'] = 'Arial 10'
            #Rodando o cronômetro
            else:
                Label_tempo['font'] = 'Times 50 bold'

                temporario = str(tempo)
                h,m,s = map(int,temporario.split(':'))
                h = int(h)
                m = int(m)
                s = int(s)

                #Incrementação dos segundos
                s+=1

                if s>= 60:
                    s=0
                    m+=1

                if m >= 60:
                    m = 0
                    h += 1
                

                s = str(0)+str(s)
                m = str(0)+str(m)
                h = str(0)+str(h)

                #Atualizando os valores
                temporario = str(h[-2:]) +':' + str(m[-2:]) +':' + str(s[-2:])

                Label_tempo['text'] = temporario

                tempo = temporario

            Label_tempo.after(1000, iniciar)
            contador += 1

    #funcao para dar inicio
    def start():
        global rodar
        rodar = True
        iniciar()

    #funcao para pausar
    def pausar():
        global rodar
        rodar = False
        iniciar()

    #funcao para reiniciar
    def reiniciar():
        global contador
        global tempo
        global rodar

        rodar=True

        #reiniciando o tempo e o contador
        contador = 0
        tempo = '00:00:00'
        Label_tempo['text'] = tempo

    #Criando Interface (Labels)
    Label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
    Label_app.place(x=20, y=5)

    Label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor3)
    Label_tempo.place(x=20, y=30)


    #Botoes
    botao_iniciar = Button(janela,command= start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    botao_iniciar.place(x=20, y=130)

    botao_pausar = Button(janela,command= pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    botao_pausar.place(x=105, y=130)

    botao_reiniciar = Button(janela,command= reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    botao_reiniciar.place(x=190, y=130)


    janela.mainloop()


#função para abrir a tela criar conta (Harthur)
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


#função usada para cadastrar o usuario no banco de dados (Larah)
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
            
            banco = sqlite3.connect('dados.sqlite')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, email text, senha text, peso FLOAT, altura FLOAT, idade FLOAT)")
            cursor.execute("INSERT INTO usuarios (nome, email, senha, peso, altura, idade) VALUES (?, ?, ?, ?, ?, ?)", (nome_usuario, novo_email, nova_senha, peso, altura, idade))
            banco.commit()
            banco.close()
            print('Tabela cadastrada!')

        except sqlite3.Error as erro:
            print("Erro nos dados: ", erro)

    imgBT_criareentrar=PhotoImage(file='imgs\\bottonCriarEntrar.png')

    botao_criareentrar = Button(tela_criarconta, bd=0, image=imgBT_criareentrar, command=cadastrar)
    botao_criareentrar.place(width=135, height=43, x=512, y=589)

    tela_criarconta.mainloop()

#função usada para abrir tela principal (Larah)
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

    try:
    
        banco = sqlite3.connect('dados.sqlite')
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE email = '{}'".format(email))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    
    except:
        tela_principal.destroy()
        erro = Label(tela_login, text='Usuário não cadastrado, tente novamente!', bg= '#FAFAFA').place(x=530, y=503)

    banco = sqlite3.connect('dados.sqlite')
    cursor = banco.cursor()
    cursor.execute("SELECT id, nome, altura, peso, idade FROM usuarios WHERE email = ?", (email,))
    user_info = cursor.fetchone()

    if user_info:
        id, nome, altura, peso, idade = user_info

#Cálculos gerais (Itamar)
    consumo = 35 * peso
    consumo = consumo / 1000

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

#função que chama o controle de água (Larah)
    def consumoagua():

        def conectar_banco():
       
            banco = sqlite3.connect('dados.sqlite')
            cursor = banco.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
            id_bd = cursor.fetchone()
            print(f'Essa é a senha: {id_bd}')
            banco.close()

            if id_bd:
                user_id = id_bd[0]

                nome_banco = f"registro_agua_{user_id}.sqlite"
                banco_agua = sqlite3.connect(nome_banco)
                cursor = banco_agua.cursor()
            
                cursor.execute("CREATE TABLE IF NOT EXISTS registros (data DATE, litros FLOAT)")
                banco_agua.commit()
                return banco_agua, cursor

        def registrar_agua():
            litros = float(entry_litros.get())
            if litros <= 0:
                return

            banco_agua, cursor = conectar_banco()
            data_atual = datetime.date.today()

            cursor.execute("SELECT * FROM registros WHERE data=?", (data_atual,))
            registro_existente = cursor.fetchone()

            if registro_existente:
                litros_total = registro_existente[1] + litros
                cursor.execute("UPDATE registros SET litros=? WHERE data=?", (litros_total, data_atual))
            else:
                cursor.execute("INSERT INTO registros (data, litros) VALUES (?, ?)", (data_atual, litros))

            banco_agua.commit()
            banco_agua.close()
            entry_litros.delete(0, END)  

        #função de criação do gráfico de registros de água (Rita)
        def exibir_registros_semana():
            banco_agua, cursor = conectar_banco()
            data_atual = datetime.date.today()
            data_inicio_semana = data_atual - datetime.timedelta(days=data_atual.weekday())
            data_fim_semana = data_inicio_semana + datetime.timedelta(days=6)

            cursor.execute("SELECT * FROM registros WHERE data BETWEEN ? AND ?", (data_inicio_semana, data_fim_semana))
            registros_semana = cursor.fetchall()

            banco_agua.close()

            datas = [registro[0] for registro in registros_semana]
            litros = [registro[1] for registro in registros_semana]

            cor_das_barras = 'green'
            fonte = 'Cambria'
            plt.bar(datas, litros, color= cor_das_barras)
            plt.xlabel("Data", fontdict={'fontsize': 14, 'fontname': fonte})
            plt.ylabel("Litros", fontdict={'fontsize': 14, 'fontname': fonte})
            plt.title("Consumo de Água na Semana", fontdict={'fontsize': 14, 'fontname': fonte})
            plt.xticks(rotation=45)
            plt.show()

            texto_registros.delete(1.0, END)  
            for registro in registros_semana:
                data, litros = registro
                texto_registros.insert(END, f'Data: {data}, Litros: {litros}\n')

        janela = Tk()
        janela.title("Registro de Consumo de Água")
        janela.geometry("400x300")
        center(janela)

        label_litros = Label(janela, text="Quantidade de Litros:" )
        label_litros.pack()

        entry_litros = Entry(janela)
        entry_litros.pack()

        botao_registrar = Button(janela, text="Registrar", command=registrar_agua)
        botao_registrar.pack()

        botao_exibir_semana = Button(janela, text="Exibir Registros da Semana", command=exibir_registros_semana)
        botao_exibir_semana.pack()

        texto_registros = Text(janela, height=10, width=40)
        texto_registros.pack()

        janela.mainloop()


    def controlepeso(): #(Lucas)
        
        banco = sqlite3.connect('dados.sqlite')
        cursor = banco.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        id_bd = cursor.fetchone()
        print(f'Essa é a senha: {id_bd}')
        banco.close()
        
        if id_bd:
            user_id = id_bd[0]
            datas = datetime.date.today()

        nome_banco = f"controle_peso_{user_id}.sqlite"
        banco_agua = sqlite3.connect(nome_banco)
        cursor = banco_agua.cursor()
        data_atual = datetime.date.today()
        cursor.execute("CREATE TABLE IF NOT EXISTS pesos (data DATE, peso FLOAT)")
        banco_agua.commit()
        cursor.execute("INSERT INTO pesos (data, peso) VALUES (?, ?)", (data_atual, peso))
        banco_agua.commit()
        cursor.execute("SELECT data, peso FROM pesos")
        registros = cursor.fetchall()

        datas = [registro[0] for registro in registros]
        pesos = [registro[1] for registro in registros]

        
        fonte = 'Cambria'
        plt.plot(datas, pesos, marker='o', linestyle='-', color='green')
        plt.xlabel("Data", fontdict={'fontsize': 14, 'fontname': fonte})
        plt.ylabel("Peso", fontdict={'fontsize': 14, 'fontname': fonte})
        plt.title("Controle de Peso", fontdict={'fontsize': 14, 'fontname': fonte})
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    #visualizar os resultados na tela (Itamar)
    nome_label = Label(tela_principal, text=f"Oi, {nome}!", bg='#dadada', font=("Helvetica", 35, "bold"))
    nome_label.place(x=384, y=136) 
    basal_label = Label(tela_principal, text=f"{basal:.2f} cal.", bg='#008923', fg='#f2f6f4', font=("Roboto", 14))
    basal_label.place(x=95, y=157)  
    imc_label = Label(tela_principal, text=f"{imc:.2f} hg/m2", bg='#008923', fg='#f2f6f4', font=("Roboto", 14))
    imc_label.place(x=95, y=268)
    consumo_label = Label(tela_principal, text=f"{consumo:.2f} L", bg='#008923', fg='#f2f6f4', font=("Roboto", 14))
    consumo_label.place(x=90, y=394)

    #abrir tela de atualizar informes (Larah) 
    def atualizar_informes():
    
        tela_informes = Toplevel()
        tela_informes.geometry('1280x720')
        tela_informes.resizable(False, False)
        tela_informes.title('Heath Point')
        center(tela_informes)

        fundo_tela_informes = PhotoImage(file='imgs\\Facul-TelaNewInfo.png')
        label_informes = Label(tela_informes, image=fundo_tela_informes)
        label_informes.pack()

        pesoSeek = IntVar()
        alturaSeek = IntVar()
        idadeSeek = IntVar()

        peso = Entry(tela_informes, textvariable= pesoSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        peso.place(x=465, y=518)
        altura = Entry(tela_informes, textvariable= alturaSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        altura.place(x=465, y=424)
        idade = Entry(tela_informes, textvariable= idadeSeek, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
        idade.place(x=465, y=336)

        #atualiza os dados do banco (Larah)
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
                cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
                id_bd = cursor.fetchone()
                print(f'Essa é a senha: {id_bd}')
                banco.close()
        
                if id_bd:
                    user_id = id_bd[0]

                    nome_banco = f"controle_peso_{user_id}.sqlite"
                    banco_agua = sqlite3.connect(nome_banco)
                    cursor = banco_agua.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS pesos (data DATE, peso FLOAT)")
                    banco_agua.commit()
                    banco_agua.close()

            except sqlite3.Error as erro:
                print("Erro nos dados: ", erro)

        fundobotao = PhotoImage(file='imgs\\Facul-BottonSalvar.png')
        botao = Button(tela_informes, image=fundobotao, borderwidth=0, command=atualizar)
        botao.place(x=572, y=574)
    
        tela_informes.mainloop()

    fundo_botao_novasmedidas = PhotoImage(file='imgs\\medidasBotton.png')
    fundo_botao_meditacao = PhotoImage(file='imgs\\mediteBotton.png')
    fundo_botao_consumo = PhotoImage(file='imgs\\waterBotton.png')
    fundo_botao_controlepeso = PhotoImage(file='imgs\\pesoBotton.png') 

    botao_novasmedidas = Button(tela_principal, width=180, height=53, image=fundo_botao_novasmedidas, borderwidth=0, command=atualizar_informes)
    botao_novasmedidas.place(x=32, y=495)
    botao_meditacao = Button(tela_principal, width=214, height=233, image=fundo_botao_meditacao, borderwidth=0, command=abrir_meditacao)
    botao_meditacao.place(x=348, y=385)
    botao_consumo = Button(tela_principal, width=214, height=233, image=fundo_botao_consumo, borderwidth=0, command=consumoagua)
    botao_consumo.place(x=660, y=385)
    botao_controlepeso = Button(tela_principal, width=214, height=233, image=fundo_botao_controlepeso, borderwidth=0, command=controlepeso)
    botao_controlepeso.place(x=969, y=385)

    tela_principal.mainloop()


#conteúdo tela de login (Harthur)

tela_login.geometry('1280x720')
tela_login.resizable(False, False)
tela_login.title('Health Point')
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
