#   Mateus 18/01/2023
#   Estudo de classes

class Dog():
    '''Uma tentativa siples de modelar um cachorro'''

#   Definindo os atributos da instancia
    def __init__(self, name, age):
        '''inicializa os atributos name e age'''
        self.name = name
        self.age = age

#   Definindo os métodos da instância
    def sit(self):
        '''Simula um cachorro sentando em resposta a um comando'''
        print(self.name.title() + " is now siting.")

    def roll_over(self):
        '''Simula o cachorro rolando em resposta a um comando'''
        print(self.name.title() + " rolled over!")


class Pizza():
    def __init__(self, ingredientes, tamanho):
        self.ingredientes = ingredientes
        self.tamanho = tamanho
    pass

pizza1 = Pizza('presunto', 30)
pizza2 = Pizza('calabresa', 40)



class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def Informações_carro(self):
        '''Exibe as informações do carro'''
        print(self.marca.title(), self.modelo.title(), self.ano)

    def acelerar(self):
        print("Estou acelerando")
    
    def frear(self):
        print("Estou freando")

    def leitura_odometro(self):
        '''Exibe uma frase que mostra o odometro do carro'''
        print("Esse carro está com " + str(self.odometro) +
         " quilometros rodados.")

    def atualizar_odometro(self, quilometragem):
        '''Define o valor de leitura do odometro com o valor especificado'''
        '''Rejeita a alteração se for tentativa de dimnuir o valor do odometro'''
        if quilometragem >= self.odometro:
            self.odometro = quilometragem
        else:
            print("Você nao pode diminuir o valor do odometro.")

    def incrementar_odometro(self, quilometros):
        '''soma mais quilometros ao odômetro conforme'''
        self.odometro += quilometros

carro1 = Carro('ford','ka', 2017)

 # Alterando um valor de atributo diretamente
carro1.odometro = 40   
carro1.leitura_odometro()

# Alterando o valor de atributo com o método definido dentro da classe
carro1.atualizar_odometro(500)
carro1.leitura_odometro()

# Forçando a mensagem de erro ao mudar a quilometragem
carro1.atualizar_odometro(450)

# Incrementando mais quilometros 
carro1.incrementar_odometro(700)
carro1.leitura_odometro()


#   Heranças em classes

# Criando uma 'classe-filha'
class CarroEletrico(Carro):
    '''Representa aspectos específicos de veiculos eletricos'''

    def __init__(self, marca, modelo, ano):
        '''inicializa os atributos da (classe-pai)'''
        super().__init__(marca, modelo, ano)


my_tesla = CarroEletrico('tesla','model s', 2016)
my_tesla.Informações_carro()

# Acrescentando um método e um atributo novo à classe-filha
class CarroEletrico(Carro):
    '''Representa aspectos específicos de veiculos eletricos'''

    def __init__(self, marca, modelo, ano):
        '''inicializa os atributos da (classe-pai)'''
        super().__init__(marca, modelo, ano)
        self.bateria = 100

    def descricao_bateria(self):
        '''Exibe uma frase que descreve a capacidade da bateria'''
        print("O carro "+ self.modelo + " tem " + str(self.bateria) + " -Kwh.")

my_tesla = CarroEletrico('tesla','model s', 2017)
my_tesla.descricao_bateria()
    

'''exemplo de Composição'''
'''a existencia da classe 'Pedido' depende dos objetos 'Cliente' e 'Produto' '''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def exibir_info(self):
        print("Nome: " + self.nome.title())
        print("E-mail: " + self.email)
        print("Endereço: " + self.endereco.title())

class Pedido:
    def __init__(self, cliente, produtos):
        self.produtos = produtos
        self.cliente = cliente

    def exibir_info(self):
        self.cliente.exibir_info()
        print("Produtos: ")
        for produto in self.produtos:
            print(produto.nome.title() + " - preço - " + str(produto.preco))




cliente1 = Cliente('mateus', 'mateus@gmail.com', 'rua benedito pereira')
tv = Produto('televisao', 1200)
radio = Produto('radio', 160)

produtos = [tv, radio]
pedido = Pedido(cliente1, produtos)
pedido.exibir_info()