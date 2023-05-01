#Simulador de Dado
import random #Bibloteca que gera valores aleatorios

class SimuladorDedado:
    def __init__(self) -> None: #Objeto da Classe simulador de dado
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de Girar o Dado ?'
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.GerarValorDoDado()

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))