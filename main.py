from tkinter import * 
 

tela_login = Tk()

#funções usadas

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

def abrirtela_criarconta():

    tela_login.destroy()
    
    tela_criarconta= Tk()
    tela_criarconta.geometry('1280x720')
    tela_criarconta.resizable(False, False)
    tela_criarconta.title('Heath Point')
    center(tela_criarconta)

    fundo_tela_criarconta = PhotoImage(file='imgs\\criar.png')
    label_login = Label(tela_criarconta, image=fundo_tela_criarconta)
    label_login.pack()
    

    senhaSeek= StringVar()

    nome_usuario = Entry(tela_criarconta, width=32, bg='#dadada', borderwidth='0', font='Arial''11') 
    nome_usuario.place(x=465, y=336)
    novo_email = Entry(tela_criarconta, width=32, bg='#dadada', borderwidth='0', font='Arial''11')
    novo_email.place(x=465, y=424)
    nova_senha = Entry(tela_criarconta, textvariable=senhaSeek, show= "*", width=32,bg='#dadada', borderwidth='0', font='Arial''11')
    nova_senha.place(x=465, y=518)

    imgBT_criareentrar=PhotoImage(file='imgs\\bottonCriarEntrar.png')

    botao_criareentrar = Button(tela_criarconta, bd=0, image=imgBT_criareentrar, command=abrirtela_principal)
    botao_criareentrar.place(width=135, height=43, x=571, y=572)

    tela_criarconta.mainloop()

def abrirtela_principal():

    tela_login.destroy()
    
    tela_principal= Tk()

    tela_principal.geometry('1280x720')
    tela_principal.resizable(False, False)
    tela_principal.title('Página Principal')
    center(tela_principal)
    
    fundo_tela_principal = PhotoImage(file='imgs\\')
    label_tela_principal = Label(tela_principal, image=fundo_tela_principal)
    label_tela_principal.pack()

    tela_principal.mainloop()

#conteúdo primeira tela

tela_login.geometry('1280x720')
tela_login.resizable(False, False)
tela_login.title('Heath Point')
tela_login.iconbitmap(default='imgs\\appi.ico')
center(tela_login)

fundo_tela_login = PhotoImage(file='imgs\\login.png')
Label_login = Label(tela_login, image=fundo_tela_login).pack()

senhaSeek= StringVar()

email = Entry(tela_login, width=32, bg='#dadada', borderwidth='0', font='Arial''11').place(x=465, y=360)
senha = Entry(tela_login, textvariable=senhaSeek, show= "*", width=32,bg='#dadada', borderwidth='0', font='Arial''11').place(x=465, y=464)

imgBT_criarconta=PhotoImage(file='imgs\\bottonCriar.png')
imgBT_entrar=PhotoImage(file='imgs\\bottonEntrar.png')

botao_criarconta=Button(tela_login, bd=0, image=imgBT_criarconta, command= abrirtela_criarconta)
botao_criarconta.place(width=135, height=43, x=652, y=536)

botao_entrar=Button(tela_login, bd=0, image=imgBT_entrar, command=abrirtela_principal)
botao_entrar.place(width=135, height=43, x=490, y=536)

tela_login.mainloop()
