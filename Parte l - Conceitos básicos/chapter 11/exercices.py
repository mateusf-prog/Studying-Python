import unittest

class Empregado():
    def __init__(self, p_nome, s_nome, salario_anual):
        self.p_nome = p_nome
        self.s_nome = s_nome
        self.salario_anual = salario_anual

    def aumentar_salario(self, valor=5000):
        '''aumenta o salario do empregado'''
        if valor:
            self.salario_anual += valor
        return self.salario_anual

class TestEmpregado(unittest.TestCase):
    '''teste para a classe Epregado'''
    def setUp(self):
        '''cria uma instancia da classe a ser testada, para ser usada
        nos métodos de teste'''
        self.empregado1 = Empregado('mateus', 'fonseca', 40000)

    def test_aumentar_salario_default(self):
        '''teste para verificar se o valor default funciona'''
        self.assertEqual(self.empregado1.aumentar_salario(), 45000)

    def test_aumentar_salario_custom(self):
        '''teste para verificar se um valor diferente funciona'''
        self.assertEqual(self.empregado1.aumentar_salario(20000), 60000)


unittest.main()










