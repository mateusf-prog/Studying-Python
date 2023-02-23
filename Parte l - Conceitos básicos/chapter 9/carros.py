''' Uma classe que pode ser usada para representar um carro'''

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


class Bateria:
    def __init__(self, tamanho_bateria=70):
        '''inicializa os atributos da bateria'''
        self.tamanho_bateria = tamanho_bateria

    def descricao_bateria(self):
        '''descreve a capacidade da bateria'''
        print("Esse carro tem " + str(self.tamanho_bateria) + " -Kwh")
    
    def distancia_carga(self):
        if self.tamanho_bateria == 70:
            distancia = 240
        elif self.tamanho_bateria == 85:
            distancia = 270
        
        message = "Esse carro pode percorrer aproximadamente " + str(distancia)
        message += " quilometros com pequena carga"
        print(message)

    def atualizar_bateria(self, valor):
        if valor != 85:
            self.tamanho_bateria = 85

    
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        '''inicializa os atributos da classe-pai. em seguida, 
        inicializa os atributos especificos de um carro eletrico'''
        super().__init__(marca, modelo, ano)
        self.bateria = Bateria()


