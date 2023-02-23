#   Mateus 24/01/2023
#
#   Bibliotecas-padrão de Python
# Usando uma classe de ordenação de dicionário
'''do módulo (collections) importe a classe (OrderedDict())'''
from collections import OrderedDict

linguagem_favorita = OrderedDict()

linguagem_favorita['jen'] = 'python'
linguagem_favorita['sarah'] = 'C#'
linguagem_favorita['edward'] = 'ruby'
linguagem_favorita['phill'] = 'python'

for name, linguagem in linguagem_favorita.items():
    print(name.title() + " gosta de " + linguagem.title())

# Usando uma função que gera um número aleatório
'''do módulo (random) importe a função (randint)'''
from random import randint

class Dado:
    def __init__(self, dados=6):
        self.dados = dados

    def rolar_dados(self):
        '''rolando os dados'''
        res = randint(1, self.dados)
        for i in range(0, 3):
            print("Rolando...")
        print(res)

dado = Dado(10)
dado.rolar_dados()
dado20 = Dado(20)
dado20.rolar_dados()