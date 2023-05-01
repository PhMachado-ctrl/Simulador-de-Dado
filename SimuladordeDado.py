#Simulador de Dado
import random #Bibloteca que gera valores aleatorios
import PySimplGUI #Bliblioyeca de tela e interface

class SimuladorDedado:
    def __init__(self) -> None: #Objeto da Classe simulador de dado
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de Girar o Dado ? \n'
        # Layout
       
        # criar uma janela
        # ler os valores da tela
        # fazer alguma coisa com esses valores

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print("Agradecemos a sua participação")
            else:
                print('Favor Digitar sim ou não')
        except:
            print("Ocorreu um erro ao receber uma resposta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo)) #Escolhe um valor aleatório entre ovalor minimo e maximo

'''Para instanciar a classe'''
simulador = SimuladorDedado()
simulador.Iniciar()