#Interface gráfica
from tkinter import *
import tkinter

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