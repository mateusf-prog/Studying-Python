import unittest
from cidade_pais import cidade_e_pais

class NameTestCase(unittest.TestCase):
    def teste_cidade_pais(self):
        '''funciona com "São José Dos Campos, Brasil"?'''
        nome_formatado = cidade_e_pais('são josé dos campos', 'brasil')
        self.assertEqual(nome_formatado, 'São José Dos Campos, Brasil')

    def teste_cidade_pais_population(self):
        '''a funçao funciona com "São José dos Campos, Brasil - 726000"?'''
        nome_formatado = cidade_e_pais('são josé dos campos', 'Brasil', 726000)
        self.assertEqual(nome_formatado, 'São José Dos Campos, Brasil - 726000')

unittest.main()