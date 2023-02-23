#   Mateus 30/01/2023

'''     Testando o código   cap.11    '''
import unittest

# Criando uma função simples para ser testada com 'unittest'
def criar_nome_formatado(first, last):
    ''' Gera um nome formatado de modo elegante'''
    full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        '''nomes como "Mateus Fonseca" funcionam?'''
        nome_formatado = criar_nome_formatado('mateus', 'fonseca')
        self.assertEqual(nome_formatado, 'Mateus Fonseca')

unittest.main()                
#Resultado do teste = Ok


# Alterando a função a ser testada, de modo que aceite um nome do meio
# e que esse nome seja opcional, fazendo assim o teste continuar passando

def criar_nome_formatado(first, last, middle=''):
    ''' Gera um nome formatado de modo elegante'''
    if middle:
        full_name = first + ' ' + middle + ' ' +last
    else:
        full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        '''nomes como "Mateus Fonseca" funcionam?'''
        nome_formatado = criar_nome_formatado('mateus', 'augusto', 'fonseca')
        self.assertEqual(nome_formatado, 'Mateus Fonseca')
    
    def test_first__last_middle_name(self):
        '''Nomes como "Mateus Augusto Ribeiro" funcionam?'''
        nome_formatado = criar_nome_formatado('mateus', 'augusto', 'ribeiro')
        self.assertEqual(nome_formatado, 'Mateus Augusto')      

unittest.main()