#   Mateus 20/01/2023
#   Exercices


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

sabor_mineiro = Restaurante('sabor mineiro', 'média')
sabor_mineiro.descricao()
sabor_mineiro.mudar_quantidade_atendidos(300)
sabor_mineiro.mudar_quantidade_atendidos(500)

prato_fino = Restaurante('prato fino','grande')
prato_fino.descricao()
prato_fino.mudar_quantidade_atendidos(100)
prato_fino.mudar_quantidade_atendidos(50)
print("\n\n")


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


user1 = User('mateus','fonseca', 25, 'mateus102006@hotmail.com')
user2 = User('tainara','rayane', 22, 'tayrayane26@yahoo.com')

user1.saudacoes()
user2.saudacoes()
user1.incrementar_tentativas_login(4)
user1.incrementar_tentativas_login(3)
user1.reset_tentativas_login()
user1.incrementar_tentativas_login(2)
