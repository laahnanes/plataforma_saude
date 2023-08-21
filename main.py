from tkinter import * 
from PIL import ImageTk, Image
 

tela_login = Tk()

#funções usadas

def abrirtela_criarconta():

    tela_login.destroy()
    
    tela_criarconta= Tk()
    largura = tela_criarconta.winfo_screenwidth()  
    altura = tela_criarconta.winfo_screenheight() 
    tela_criarconta.geometry(f'{largura}x{altura}')
    tela_criarconta.resizable(False, False)
    tela_criarconta.title('Heath Point')

    fundo_tela_criarconta_pil = Image.open('imgs\\Facul-TelaCriar.jpg')
    fundo_tela_criarconta_pil = fundo_tela_criarconta_pil.resize((largura, altura))
    fundo_tela_criarconta = ImageTk.PhotoImage(fundo_tela_criarconta_pil)
    label_criarconta = Label(tela_criarconta, image=fundo_tela_criarconta)
    label_criarconta.pack()

    senhaSeek= StringVar()

    nome_usuario = Entry(tela_criarconta, width=32, bg='#dadada', borderwidth='0', font='Arial''11') 
    nome_usuario.place(x=562, y=407)
    novo_email = Entry(tela_criarconta, width=37, bg='#dadada', borderwidth='0', font='Arial''11')
    novo_email.place(x=564, y=511)
    nova_senha = Entry(tela_criarconta, textvariable=senhaSeek, show= "*", width=37,bg='#dadada', borderwidth='0', font='Arial''11')
    nova_senha.place(x=564, y=625)

    imgBT_criareentrar=PhotoImage(file='imgs\\BottonCreEntry.png')

    botao_criareentrar = Button(tela_criarconta, bd=0, image=imgBT_criareentrar, command=abrirtela_principal)
    botao_criareentrar.place(width=203, height=63, x=669, y=681)


    tela_criarconta.mainloop()

def abrirtela_principal():

    tela_login.destroy()
    
    tela_principal= Tk()

    largura = tela_principal.winfo_screenwidth()  
    altura = tela_principal.winfo_screenheight() 
    tela_principal.geometry(f'{largura}x{altura}')
    tela_principal.resizable(False, False)
    tela_principal.title('Página Principal')

    fundo_tela_principal_pil = Image.open('')
    fundo_tela_principal_pil = fundo_tela_principal_pil.resize((largura, altura))
    fundo_tela_principal = ImageTk.PhotoImage(fundo_tela_principal_pil)
    label_tela_principal = Label(tela_principal, image=fundo_tela_principal)
    label_tela_principal.pack()


    tela_principal.mainloop()

#conteúdo primeira tela

largura = tela_login.winfo_screenwidth()  
altura = tela_login.winfo_screenheight() 
tela_login.geometry(f'{largura}x{altura}')
tela_login.resizable(False, False)
tela_login.title('Heath Point')
tela_login.iconbitmap(default='imgs\\appi.ico')

#imgBT_criareentrar=PhotoImage(file='imgs\\BottonCreEntry.png')

fundo_tela_login_pil = Image.open('imgs\\Facul-TelaLogin.jpg')
fundo_tela_login_pil = fundo_tela_login_pil.resize((largura, altura))
fundo_tela_login = ImageTk.PhotoImage(fundo_tela_login_pil)
Label_pri = Label(tela_login, image=fundo_tela_login).pack()

senhaSeek= StringVar()

email = Entry(tela_login, width=37, bg='#dadada', borderwidth='0', font='Arial''11').place(x=564, y=430)
senha = Entry(tela_login, textvariable=senhaSeek, show= "*", width=37,bg='#dadada', borderwidth='0', font='Arial''11').place(x=564, y=555)

imgBT_criarconta=PhotoImage(file='imgs\\BottonCreate.png')
imgBT_entrar=PhotoImage(file='imgs\\BottonEntry.png')

botao_criarconta=Button(tela_login, bd=0, image=imgBT_criarconta, command= abrirtela_criarconta)
botao_criarconta.place(width=203, height=63, x=780, y=640)

botao_entrar=Button(tela_login, bd=0, image=imgBT_entrar, command=abrirtela_principal)
botao_entrar.place(width=203, height=63, x=553, y=640)

tela_login.mainloop()
