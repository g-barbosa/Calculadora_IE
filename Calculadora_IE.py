from tkinter import *
from Calculos import Calculos


def op1():
    botao_lamp_tom.place_forget()
    pergunta1.pack_forget()
    pergunta2 = Label(janela, text="CÔMODO: ")
    pergunta3 = Label(janela, text="LARGURA(m): ")
    pergunta4 = Label(janela, text="COMPRIMENTO(m): ")

    pergunta2["bg"] = "grey"  # muda a cor do background
    pergunta2["font"] = ("Arial black", "10", "bold")  # muda a fonte
    pergunta3["bg"] = "grey"  # muda a cor do background
    pergunta3["font"] = ("Arial black", "10", "bold")  # muda a fonte
    pergunta4["bg"] = "grey"  # muda a cor do background
    pergunta4["font"] = ("Arial black", "10", "bold")  # muda a fonte

    pergunta2.grid(row=0, column=0)  # define as perguntas em grids
    pergunta3.grid(row=1, column=0)
    pergunta4.grid(row=2, column=0)

    entrada_comodo = Entry(janela, width=25)
    entrada_largura = Entry(janela, width=25)
    entrada_comprimento = Entry(janela, width=25)
    entrada_comodo.grid(row=0, column=1)
    entrada_largura.grid(row=1, column=1)
    entrada_comprimento.grid(row=2, column=1)

    def calcula():
        comodo = entrada_comodo.get()
        largura = float(entrada_largura.get())
        comprimento = float(entrada_comprimento.get())

        local = Calculos(comodo, largura, comprimento)
        area = local.calculo_area()
        perimetro = local.calculo_perimetro()
        pot = local.potmin_lamp()
        tom = local.qntmin_tom()

        resultado = Label(janela)
        resultado["text"] = ("CÔMODO: %s\nAREA: %.2f m²\nPERIMETRO: %.2f m\nPOTENCIA MINIMA DE LAMPADAS: %d VA\nQUANTIDADE MINIMA DE TOMADAS: %d TOMADA(S)"%(local.comodo, area, perimetro, pot, tom))
        resultado["bg"] = "Grey"
        resultado["font"] = ("arial black", "8", "bold")
        resultado.place(x=0, y=110)

    botao_ok = Button(janela, text="OK")
    botao_ok["command"] = calcula
    botao_ok.place(x=144, y=80)
    botao_ok["bg"] = "LightGrey"


janela = Tk()
janela.title("CALCULADORA INSTALAÇÕES ELÉTRICAS")
janela['bg'] = 'grey'

pergunta1 = Label(janela, text="O QUE DESEJA SABER?\n")
pergunta1.pack()  # posiciona o texto no centro
pergunta1["bg"] = "Grey"  # muda a cor do background
pergunta1["fg"] = "black"
pergunta1["font"] = ("Arial black", "10", "bold")  # muda a fonte

botao_lamp_tom = Button(janela, width=30, text="POTÊNCIA MÍNIMA DAS LÂMPADAS \n E QUANTIDADE MÍNIMA DE TOMADAS")
botao_lamp_tom["command"] = op1
botao_lamp_tom.place(x=50, y=100)
botao_lamp_tom["bg"] = "LightGrey"


janela.geometry("320x250+550+200")  # dimensoes da janela LxA+margemE+Topo
janela.mainloop()
