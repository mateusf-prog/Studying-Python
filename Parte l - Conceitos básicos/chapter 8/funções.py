#   Mateus 10/01/2023
#   Funções
def cumprimentos(username):
    print("Hello " + username.title() + "!")
cumprimentos('mateus')
# A variável 'username' é um parâmetro e 'mateus' é um argumento
# Nesse caso, o argumento 'mateus' foi passado para a função cumprimentos()
# e o valor foi armazenado no parâmetro 'username'.
#
#
def display_message():
    print("\nOlá pessoal!")
display_message()
#
#
def livro_favorito(livro):
    print("\nMeu livro favorito é " + livro.title())
   
livro_favorito('mundo python')
livro_favorito('2º guerra mundial em cores')
#
#
#   Argumentos posicionais
def descricao_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação"""
    print("\nEu tenho um " + animal_type + ".")
    print("Meu " + animal_type + " tem o nome de " + pet_name.title() + ".")
descricao_pet('cachorro', 'maya')
#
#  Nessa chamada de função o argumento 'cachorro' é armazenado no parâmetro
#  'animal_type' e o argumento 'maya' é armazenado no parâmetro 'pet_name'.
#
#   SEMPRE TOMAR CUIDADO COM A ORDEM DOS ARGUMENTOS
#
descricao_pet('mavi', 'cachorro')
print("\n\n\n")
#
#
#   Argumentos nomeados
def descricao_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação"""
    print("\nEu tenho um " + animal_type + ".")
    print("Meu " + animal_type + " tem o nome de " + pet_name.title() + ".")
descricao_pet(animal_type = 'cachorro', pet_name = 'maya')
print("\n\n\n")
#
#
#   Valores Default
def descricao_pet(pet_name, animal_type = 'cachorro'):
    """Exibe informações sobre um animal de estimação"""
    print("\nEu tenho um " + animal_type + ".")
    print("Meu " + animal_type + " tem o nome de " + pet_name.title() + ".")
descricao_pet('maya')
#
#   Alterando o tipo de animal, caso necessário, somente nessa chamada
descricao_pet(animal_type = 'gato', pet_name = 'charlie')
#
#
#   O valor default continua o mesmo = "animal_type = 'cachorro'"
descricao_pet('maya')
print("\n\n\n")
#
#
#   Devolvendo um valor simples
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('michael', 'jackson')
print(musician)
#
#
#   Deixando um argumento opcional
def get_formatted_name(first_name,middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('michael','L. ', 'jackson')
print(musician)
#
#
#   Caso não queira usar o nome do meio (Argumento opcional)
def get_formatted_name(first_name, last_name, middle_name = ''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musico = get_formatted_name('nick', 'minaj')
print(musico)
print("\n\n")
#
#
#   Devolvendo um dicionário
def pessoa(primeiro_nome, segundo_nome):
    pessoa = {'first': primeiro_nome, 'last': segundo_nome}
    return pessoa
artista = pessoa('Joao', 'neto',)
print(artista)

while True:
    print("Por favor, me diga seu nome: ")
    f_name = input("Primeiro nome: ")
    l_name = input("Sobrenome: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nOlá, " + formatted_name + "!")
    break
#
#
