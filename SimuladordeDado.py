#Simulador de Dado
import random #Bibloteca que gera valores aleatorios
import PySimpleGUI as sg #Bliblioyeca de tela e interface

class SimuladorDedado:
    def __init__(self)-> None: #Objeto da Classe simulador de dado
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de Girar o Dado ? \n'
        # Layout
        self.layout = [
            [sg.Text("Jogar um Dado?")],
            [sg.Button("sim"), sg.Button("não")]
        ]
       
      
        # fazer alguma coisa com esses valores
    def Iniciar(self):
         # criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
          # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == "sim" or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == "não" or self.eventos == 'n':
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