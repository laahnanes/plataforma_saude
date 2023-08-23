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

def abrirtela_informes():

    tela_informes= Toplevel()
    tela_informes.geometry('1280x720')
    tela_informes.resizable(False, False)
    tela_informes.title('Heath Point')
    center(tela_informes)

    fundo_tela_informes = PhotoImage(file='imgs\\infor.png')
    label_informes = Label(tela_informes, image=fundo_tela_informes)
    label_informes.pack()

    peso = Entry(tela_informes, width=37, bg='#dadada', borderwidth='0', font='Arial''11')
    peso.place(x=480, y=339)
    altura = Entry(tela_informes, width=37, bg='#dadada', borderwidth='0', font='Arial''11')
    altura.place(x=480, y=428)
    idade = Entry(tela_informes, width=37, bg='#dadada', borderwidth='0', font='Arial''11')
    idade.place(x=470, y=516)

    tela_informes.mainloop()

#conteúdo primeira tela

tela_login.geometry('1280x720')
tela_login.resizable(False, False)
tela_login.title('Heath Point')
tela_login.iconbitmap(default='imgs\\appi.ico')
center(tela_login) 

fundo_tela_login = PhotoImage(file='imgs\\login.png')
Label_login = Label(tela_login, image=fundo_tela_login).pack()

senhaSeek= StringVar()

email = Entry(tela_login, width=37, bg='#dadada', borderwidth='0', font='Arial''11').place(x=472, y=360)
senha = Entry(tela_login, textvariable=senhaSeek, show= "*", width=37,bg='#dadada', borderwidth='0', font='Arial''11').place(x=472, y=464)

imgBT_criarconta=PhotoImage(file='imgs\\bottonCriar.png')
imgBT_entrar=PhotoImage(file='imgs\\bottonEntrar.png')

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
    
    nome_usuario = Entry(tela_criarconta, width=37, bg='#dadada', borderwidth='0', font='Arial''11') 
    nome_usuario.place(x=480, y=339)
    novo_email = Entry(tela_criarconta, width=37, bg='#dadada', borderwidth='0', font='Arial''11')
    novo_email.place(x=480, y=428)
    nova_senha = Entry(tela_criarconta, width=37,bg='#dadada', borderwidth='0', font='Arial''11')
    nova_senha.place(x=470, y=516)

    imgBT_criareentrar=PhotoImage(file='imgs\\bottonCriarEntrar.png')

    botao_criareentrar = Button(tela_criarconta, bd=0, image=imgBT_criareentrar, command=abrirtela_informes)
    botao_criareentrar.place(width=135, height=43, x=572, y=573)

    tela_criarconta.mainloop()

botao_criarconta=Button(tela_login, bd=0, image=imgBT_criarconta, command= abrirtela_criarconta)
botao_criarconta.place(width=135, height=43, x=652, y=536)

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

botao_entrar=Button(tela_login, bd=0, image=imgBT_entrar, command=abrirtela_principal)
botao_entrar.place(width=135, height=43, x=490, y=536)

tela_login.mainloop()
