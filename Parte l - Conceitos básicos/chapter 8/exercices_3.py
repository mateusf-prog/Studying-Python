#   Mateus 17/01/2023
#   Exercicios cap.8

def sanduiche(*ingredientes):
    print("Preparando sanduíche com os ingredientes: ")
    for ingrediente in ingredientes:
        print("- " + ingrediente.title())
    
sanduiche('alface','queijo','presunto')
sanduiche('tomate','presunto')
sanduiche('maionese')
#
#
def new_user(nome, sobrenome, **infos):
    perfil = {}
    perfil['nome'] = nome
    perfil['sobrenome'] = sobrenome
    for chave, valor in infos.items():
        perfil[chave] = valor
    return perfil

user = new_user('mateus', 'augusto', idade=25, altura=1.80, cidade='sjc')
print(user)
#
#
def cars(fabricante, modelo, **infos):
    car = {}
    car['fabricante'] = fabricante
    car['modelo'] = modelo
    for key, value in infos.items():
        car[key] = value
    return car

car = cars('ford','fusion', cor='branco', ano=2020)
print(car)