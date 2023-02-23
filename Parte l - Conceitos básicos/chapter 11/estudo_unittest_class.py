'''         Testando uma classe cap.11        '''
import unittest

class PesquisaAnonima():
    '''coleta as respostas anonimas para uma pergunta de uma pesquisa'''

    def __init__(self, pergunta):
        '''armazena uma pergunta e se prepara para armazenar uma resposta'''
        self.pergunta = pergunta
        self.respostas = []

    def mostrar_pergunta(self):
        '''mostra a pergunta da pesquisa'''
        print(self.pergunta)

    def armazenar_resposta(self, nova_resposta):
        '''armazena a unica resposta da pesquisa'''
        self.respostas.append(nova_resposta)
    
    def mostrar_resultados(self):
        '''mostra todas as respostas dadas.'''
        print("Mostrando respostas:")
        for resposta in self.respostas:
            print("- " + resposta)

class TestPesquisaAnonima(unittest.TestCase):
    '''testes para a classe "PesquisaAnonima"'''

    def test_armazenamento_uma_resposta(self):
        '''teste se uma resposta unica é armazenada de forma correta'''
        pergunta = "Qual seu nome?"
        minha_enquete = PesquisaAnonima(pergunta)
        minha_enquete.armazenar_resposta('Mateus')
        self.assertIn('Mateus', minha_enquete.respostas) 

    def test_armazenamento_tres_repostas(self):
        '''testa se três respostas individuais são armazenadas de forma
        apropriada'''
        pergunta = "Qual seu nome?"
        minha_enquete = PesquisaAnonima(pergunta)
        respostas = ['mateus', 'tainara', 'jessica']
        for reposta in respostas:
            minha_enquete.armazenar_resposta(reposta)
        for resposta in respostas:
            self.assertIn(resposta, minha_enquete.respostas)







