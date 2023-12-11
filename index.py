from tkinter import *

janela = Tk()
janela.title('Calculadora')
janela.geometry('400x600')

#tela

frameTela = Frame(janela, width= 355, height=90, bg='#e5e5e5')
frameTela.place(x=20, y=10)

digito = ''
n = 0
cor = '#00aaf9'
resultado = 0
#função

def entrada(codigo):
    global digito
    print(codigo)

    if codigo == 'CE':
       digito = ''
       codigo = ''

    if codigo == '=':
       resultado= eval(digito)
       digito=''
       digito = digito+str(resultado)
       visorStr.set(digito)


    if codigo != '=' and codigo != 'CE':
       digito = digito+ str(codigo)
       visorStr.set(digito)


#visor

visorStr =StringVar()
visor = Label(frameTela, textvariable = visorStr)
visor.configure(font=("Arial", 30,), bg='#e5e5e5')
visor.place(x= 0, y=50)

#botão primeira fileira

porcetagem = Button(janela, command= lambda: entrada('%'), text='%', width=10, height= 5, relief='flat', fg='black', bg='#e5e5e5')
porcetagem.place(x= 295, y= 110)

divisao = Button(janela, command= lambda: entrada('//'), text='÷',  width=10, height= 5, relief='flat', fg='black', bg='#e5e5e5')
divisao.place(x=205, y= 110)

c = Button(janela, command= lambda: entrada('CE'), text='CE', width=23, height= 5, relief='flat', fg='black', bg='#e5e5e5')
c.place(x=20, y= 110)

#segunda fileira

sete = Button(janela, command= lambda: entrada('7'), text='7', width=10, height= 5, relief='flat', fg='black', bg='white')
sete.place(x=20, y= 210)

oito = Button(janela, command= lambda: entrada('8'), text='8', width=10, height= 5, relief='flat', fg='black', bg='white')
oito.place(x=115, y= 210)

nove = Button(janela, command= lambda: entrada('9'), text='9', width=10, height= 5, relief='flat', fg='black', bg='white')
nove.place(x=205, y= 210)

multiplicao = Button(janela, command= lambda: entrada('*'), text='X', width=10, height= 5, relief='flat', fg='black', bg='#e5e5e5')
multiplicao.place(x=295, y= 210)

#terceiar fileira

quatro = Button(janela, text='4', command= lambda: entrada('4'), width=10, height= 5, relief='flat', fg='black', bg='white')
quatro.place(x=20, y= 310)

cinco = Button(janela, text='5', command= lambda: entrada('5'), width=10, height= 5, relief='flat', fg='black', bg='white')
cinco.place(x=115, y= 310)

seis = Button(janela, text='6', command= lambda: entrada('6'), width=10, height= 5, relief='flat', fg='black', bg='white')
seis.place(x=205, y= 310)

subtracao = Button(janela, text='-', command= lambda: entrada('-'), width=10, height= 5, relief='flat', fg='black', bg='#e5e5e5')
subtracao.place(x=295, y= 310)

#quatro

um = Button(janela, text='1', command= lambda: entrada('1'), width=10, height= 5, relief='flat', fg='black', bg='white')
um.place(x=20, y= 410)

dois = Button(janela, text='2', command= lambda: entrada('2'), width=10, height= 5, relief='flat', fg='black', bg='white')
dois.place(x=115, y= 410)

tres = Button(janela, text='3', command= lambda: entrada('3'), width=10, height= 5, relief='flat', fg='black', bg='white')
tres.place(x=205, y= 410)

adicao = Button(janela, text='+', command= lambda: entrada('+'), width=10, height= 5, relief='flat', fg='black', bg='#e5e5e5')
adicao.place(x=295, y= 410)

#cinco

zero = Button(janela, text='0', command= lambda: entrada('0'), width=23, height= 5, relief='flat', fg='black', bg='#e5e5e5')
zero.place(x=20, y= 510)

virgula = Button(janela, text=',', command= lambda: entrada('.'), width=10, height= 5, relief='flat', fg='black', bg='white')
virgula.place(x=205, y= 510)

resultado= Button(janela, text='=', command= lambda: entrada('='), width=10, height= 5, relief='flat', fg='black', bg='#00aaf9')
resultado.place(x=295, y= 510)

janela.mainloop()


