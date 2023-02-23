import unittest

def criar_nome_formatado(primeiro, segundo, terceiro=''):
    ''' Gera um nome formatado de modo elegante'''
    if terceiro:
        full_name = primeiro + ' ' + segundo + ' ' + terceiro
    else:
        full_name = primeiro + ' ' + segundo
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        '''nomes como "Mateus Fonseca" funcionam?'''
        nome_formatado = criar_nome_formatado('mateus', 'fonseca')
        self.assertEqual(nome_formatado, 'Mateus Fonseca')
    
    def test_first__last_terceiro_name(self):
        '''Nomes como "Mateus Augusto Ribeiro" funcionam?'''
        nome_formatado = criar_nome_formatado('mateus', 'augusto', 'ribeiro')
        self.assertEqual(nome_formatado, 'Mateus Augusto Ribeiro')      

unittest.main()