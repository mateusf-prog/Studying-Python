#   Mateus 23/01/2023
#   Exercicios

class Restaurante():
    
    #   Definindo os atributos
    def __init__(self, restaurante_nome, tamanho_cozinha):
        self.restaurante_nome = restaurante_nome
        self.tamanho_cozinha = tamanho_cozinha
        self.numero_servido = 0
    def descricao(self):
        '''Descreve as informações do restaurante'''
        print("Nome do restaurante: " + self.restaurante_nome.title())
        print("Tamanho da cozinha: " + self.tamanho_cozinha.title())

    def mudar_quantidade_atendidos(self, numero):
        '''Atualiza a quantidade de clientes atendidos, somando ao valor anterior'''
        self.numero_servido += numero
        print("A quantidade de clientes atendidos é de " + str(self.numero_servido) +
        " pessoas.")

class Barraca_sorvete(Restaurante):
    ''' herdou abaixo os atributos da classe-pai'''
    def __init__(self, restaurante_nome, tamanho_cozinha):
        super().__init__(restaurante_nome, tamanho_cozinha)
        self.sabores = ['chocolate','morango','maracujá']

    def mostrar_sabores(self):
        '''mostra os sabores do sorvete'''
        print("Os sabores disponíveis são: ")
        for sabor in self.sabores:
            print(sabor.title())

sorvete1 = Barraca_sorvete('Sorveteria bidu', 'grande')
sorvete1.descricao()
sorvete1.mostrar_sabores()
print("\n\n")
#
#
#
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.tentativa_login = 0

    def descricao_user(self):
        '''Descreve os dados do usuário'''
        print("Primeiro nome: " + self.first_name.title())
        print("Segundo nome: " + self.last_name.title())
        print("Idade: " + str(self.age))
        print("E-mail: " + self.email)

    def saudacoes(self):
        '''Exibe uma saudação ao usuário'''
        print("Olá " + self.first_name.title() + ", seja bem vindo(a)!")

    def incrementar_tentativas_login(self, valor):
        '''Incrementa em 1 o valor de tentativas de logins'''
        self.tentativa_login += valor
        print(str(self.tentativa_login) + " tentativas de login para " +
         self.first_name.title() + " " + self.last_name.title())

    def reset_tentativas_login(self):
        self.tentativa_login = 0 
        print("Tentativas de login resetadas para zero!")

print("\n\n")
#
#
#
class Privilegios():
    def __init__(self):
        self.privilegios = ['adicionar post','deletar post']

    def mostrar_privilegios(self):
        '''mostra os privilegios do administrador'''
        print("Os privilégios são: ")
        for privilegio in self.privilegios:
            print(privilegio)


class Admin(User):
    '''Ese método init também cria uma instancia da classe privilégios'''
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privilegios = Privilegios()

    def mostrar_privilegios(self):
        '''mostra os privilegios do administrador'''
        print("Os privilégios são: ")
        print(Privilegios)

administrador = Admin('mateus','fonseca', 25, 'mateus@hotmail.com')
administrador.privilegios.mostrar_privilegios()
