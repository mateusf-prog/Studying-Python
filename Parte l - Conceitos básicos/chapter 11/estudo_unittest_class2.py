# Utilizando o método setUp() para criar uma instância da pesquisa 
# e cria uma lista de respostas
 
import unittest
from estudo_unittest_class import PesquisaAnonima

class TestPesquisaAnonima(unittest.TestCase):
    '''testes para a classe PesquisaAnonima'''

    def setUp(self):
        '''cria uma pesquisa e um conjunto de respostas que poderão ser
        usados em todos os métodos de teste'''
        pergunta = "Qual seu nome?"
        self.minha_enquete = PesquisaAnonima(pergunta)
        self.respostas = ['Mateus', 'Sandro', 'Gabriel']

    def test_armazenamento_uma_respostas(self):
        '''testa se uma única resposta é armazenada de forma
        apropriada'''
        self.minha_enquete.armazenar_resposta(self.respostas[0])
        self.assertIn(self.respostas[0], self.minha_enquete.respostas)

    def test_armazenamento_tres_respostas(self):
        '''testa se três respostas individuais são armazenadas de
        forma apropriada'''
        for resposta in self.respostas:
            self.minha_enquete.armazenar_resposta(resposta)
        for resposta in self.respostas:
            self.assertIn(resposta, self.minha_enquete.respostas)

unittest.main()
