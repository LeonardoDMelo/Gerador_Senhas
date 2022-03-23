from email import message
from email.mime import image
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk,Image

#Importando Strings
import string
import random


#Cores-----------------------
cor1 = "#25252e" #preta
cor2 = "#6868AD" #cinza topo
cor3 = "f05a43"  #vermelha
cor4 = '#FA892C' #laranja
cor5 = '#4314FA' #azul

#Criando Janela-------------------------------
janela = Tk()
janela.title("Gerador")
janela.geometry('295x350')
janela.config(bg='white')
janela.resizable(width=FALSE,height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

#Dividindo a tela em 2 frames-----------------------
frame_cima = Frame(janela,width=295,height=50,bg=cor2,padx=0,pady=0,relief='flat')
frame_cima.grid(row=0,column=0, sticky=NSEW)


frame_baixo = Frame(janela,width=295,height=500,bg=cor1,padx=0,pady=0,relief='flat')
frame_baixo.grid(row=1,column=0, sticky=NSEW)


#trabalhando no frame cima-----------------

# img = Image.open('cadeado.png')
# img = img.resize((30,30),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(img)


# app_logo = Label(frame_cima, height=60,image=img, compound=LEFT,padx=10, relief='flat',anchor='nw',bg=cor2)
# app_logo.place(x=2,y=5)

app_nome = Label(frame_cima,text='Gerador de senhas',width=20 ,height=1,padx=0, relief='flat',anchor='nw',font='Ivy 16 bold',bg=cor2,fg='black')
app_nome.place(x=60,y=7)

app_linha = Label(frame_cima,text=' ',width=295 ,height=1,padx=0, relief='flat',anchor='nw',font='Ivy 16 bold',bg='white',fg='white')
app_linha.place(x=0,y=45)

#Variaveis da senha-----------------------------------------------------------------------------------------

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '0123456789'
simbolos = '(){}[]*;/,_-'

#Função Gerar senha------------------------------------------------------------------------------------------

def criar_senha():
    global combinar

    #Para Maiucsulo
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass
    #Para Minucsulo
    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass

        #Para numero
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    #Para simbolo
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:   
        pass

    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))


    app_senha['text'] = senha

    def copiar_senha():
        # info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(senha)

        messagebox.showinfo("Sucesso","A senha foi copiada")

    botao_copiar_senha = Button(frame_baixo,command=copiar_senha,text='Copiar',width=8,height=1,padx=0, relief='raised',anchor='center',overrelief='solid' ,font='Ivy 10',bg=cor2,fg='white')
    botao_copiar_senha.grid(row=0,column=1,sticky=NW,padx=5,pady=20,columnspan=1)


#Trabalhando Frame Baixo-------------------------------------------------------------------------------------

app_senha = Label(frame_baixo,text='- - -',width=24 ,height=2,padx=0, relief='solid',anchor='center',font='Ivy 10',bg='white',fg='black')
app_senha.grid(row=0,column=0,columnspan=1,sticky=NSEW,padx=3,pady=10)

app_info = Label(frame_baixo,text='Numero de caracteres da senha',height=1,padx=0, relief='flat',anchor='nw' ,font='Ivy 10',bg='white',fg='black')
app_info.grid(row=1,column=0,columnspan=2,sticky=NSEW,padx=5,pady=1)


#Selecionando Caracteres-------------------------------------------------------------------

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20,width=5,textvariable=var)
spin.grid(row=2,column=0,sticky=NW,padx=5,pady=5)


frame_caracter = Frame(frame_baixo,width=295,height=210,bg=cor1,padx=0,pady=0,relief='flat')
frame_caracter.grid(row=3,column=0, sticky=NSEW,columnspan=3)

#LETRAS MAIUSCULAS------------------------------------------------------------------------------------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracter,width=1,var=estado_1,onvalue=alfa_maior,offvalue='off',relief='flat',bg=cor1)
check_1.grid(row=0,column=0,padx=2,pady=6,sticky=NW)
app_info = Label(frame_caracter,text='ABC Maiusculo',height=1,padx=0, relief='flat',anchor='nw' ,font='Ivy 10',bg=cor1,fg='white')
app_info.grid(row=0,column=1,sticky=NSEW,padx=5,pady=8)

#LETRAS MINUSCULAS--------------------------------------------------------------------------------------------

estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracter,width=1,var=estado_2,onvalue=alfa_menor,offvalue='off',relief='flat',bg=cor1)
check_2.grid(row=1,column=0,padx=2,pady=6,sticky=NW)
app_info = Label(frame_caracter,text='ABC Minusculo',height=1,padx=0, relief='flat',anchor='nw' ,font='Ivy 10',bg=cor1,fg='white')
app_info.grid(row=1,column=1,sticky=NSEW,padx=5,pady=8)

#Numeros--------------------------------------------------------------------------------------------------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracter,width=1,var=estado_3,onvalue=numeros,offvalue='off',relief='flat',bg=cor1)
check_3.grid(row=2,column=0,padx=2,pady=6,sticky=NW)
app_info = Label(frame_caracter,text='123 Numeros',height=1,padx=0, relief='flat',anchor='nw' ,font='Ivy 10',bg=cor1,fg='white')
app_info.grid(row=2,column=1,sticky=NSEW,padx=5,pady=8)

#Simbolos--------------------------------------------------------------------------------------------------------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracter,width=1,var=estado_4,onvalue=simbolos,offvalue='off',relief='flat',bg=cor1)
check_4.grid(row=3,column=0,padx=2,pady=6,sticky=NW)
app_info = Label(frame_caracter,text='!@# Simbolos',height=1,padx=0, relief='flat',anchor='nw' ,font='Ivy 10',bg=cor1,fg='white')
app_info.grid(row=3,column=1,sticky=NSEW,padx=6,pady=8)


#Botão-------------------------------------------------------------------------------------------------------------

botao_gerar_senha = Button(frame_caracter,command=criar_senha,text='Gerar Senha',width=32,height=1,padx=0, relief='flat',anchor='center',overrelief='solid' ,font='Ivy 10',bg=cor2,fg='white')
botao_gerar_senha.grid(row=4,column=0,sticky=NSEW,padx=15,pady=5,columnspan=5)



janela.mainloop()