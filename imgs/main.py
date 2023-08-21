from tkinter import * 
from PIL import ImageTk, Image


tela_login = Tk()

def novatela():

    tela_login.destroy()
    
    tela2= Tk()
    largura = tela2.winfo_screenwidth()  
    altura = tela2.winfo_screenheight() 
    tela2.geometry(f'{largura}x{altura}')
    tela2.resizable(False, False)
    tela2.title('Heath Point')
    fundo_tela_home_pil = Image.open('imgs\\Facul-TelaCriar.jpg')
    fundo_tela_home_pil = fundo_tela_home_pil.resize((largura, altura))
    fundo_tela_home = ImageTk.PhotoImage(fundo_tela_home_pil)
    label_home = Label(tela2, image=fundo_tela_home)
    label_home.pack()
    tela2.mainloop()


largura = tela_login.winfo_screenwidth()  
altura = tela_login.winfo_screenheight() 
tela_login.geometry(f'{largura}x{altura}')
tela_login.resizable(False, False)
tela_login.title('Heath Point')
tela_login.iconbitmap(default='imgs\\appi.ico')

imgBT=PhotoImage(file='imgs\\BottonCreate.png')

fundo_tela_login_pil = Image.open('imgs\\Facul-TelaLogin.jpg')
fundo_tela_login_pil = fundo_tela_login_pil.resize((largura, altura))
fundo_tela_login = ImageTk.PhotoImage(fundo_tela_login_pil)
Label_pri = Label(tela_login, image=fundo_tela_login).pack()

senhaSeek= StringVar()

email = Entry(tela_login, width=37,bg='#dadada', borderwidth='0', font='Arial''11').place(x=564, y=430)
senha = Entry(tela_login, textvariable=senhaSeek, show= "*", width=37,bg='#dadada', borderwidth='0', font='Arial''11').place(x=564, y=555)


criarBT=Button(tela_login, bd=0, image=imgBT, command= novatela)
criarBT.place(width=203, height=63, x=780, y=640)

tela_login.mainloop()