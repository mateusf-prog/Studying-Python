#   Mateus 06/01/2023
#   Dicionários - cap.6
# Um dicionário é uma coleção de pares chave-valor.
#           chave     valor
alien_0 = {'color': 'green ','points':5}
# 'color' é a chave e seu valor é 'green'


# Acessando valores em um dicionário
print(alien_0['color'])
print("\n")

new_points = alien_0['points']
print ("Voce ganhou " +str(new_points) + " pontos!")
print("\n")


# Adicionando novos pares chave-valor
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")


# Começando com dicionário vazio
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print("\n")


# Modificando valores em um dicionário
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + "." + "\n")
print(alien_0)
print("\n")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']) + "\n") 
if alien_0['speed'] == 'slow':
    x_increment = 0
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print("\n")


# Removendo pares chave-valor
alien_1 = {'color': 'green', 'points': 10}
print(alien_1)
del alien_1['points']
print(alien_1)
print("\n")


# Dicionário de objetos semelhantes
favorite_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward':'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title())


# Percorrendo um dicionário com um laço 
user_0 = {
    'username': 'mateuzin',
    'first': 'mateus',
    'last': 'fonseca',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


for name, language in favorite_languages.items():
    print("\nMeu nome é: " + name.title())
    print("Minha linguagem favorita é: " + language.title())


# Percorrendo todas as chaves de um dicionário com um laço
for name in favorite_languages.keys():  # não é obrigatório colocar .keys() 
    print("\n" + name.title())


friends = ['sarah','phil']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Olá " + name.title() + 
        ", sua linguagem favoria é " + favorite_languages[name].title())


if 'erick' not in favorite_languages.keys():
    print("\nErick, por favor, escolha sua linguagem favorita! \n")


# Percorrendo as chaves de um dicionário em ordem usando um laço o método sorted()
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", obrigado por participar da pesquisa!")
# percorreu de forma ordenada


# Percorrendo todos os valores de um dicionário com um laço
for language in favorite_languages.values():
    print(language.title())
print("\n")
#
# Para extrair linguagens únicas, sem repetições de uma lista usando laço 
for language in set(favorite_languages.values()):
    print(language.title())


# Uma lista de dicionários
alien_3 = {'color': 'grreen', 'points': 5}
alien_4 = {'color': 'yellow', 'points': 10}
alien_5 = {'color': 'red', 'points': 15}
aliens = [alien_3, alien_4, alien_5]
for alien in aliens:
    print(alien)


# Criar mais aliens usando range()
aliens_novos = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_novos.append(new_alien)
print("\nForam criados mais " + str(len(aliens_novos)) + " aliens.")
for alien in aliens_novos:
    print(alien)


# Mudando as caracteristicas dos 3 primeiros aliens
for alien in aliens_novos[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens_novos[0:5]:
    print(alien)


# Uma lista em um dicionário
pizza = {
    'massa': 'leve',
    'ingredientes': ['queijo','presunto','calabresa']
}
print("\nVocê pediu uma pizza de massa " + pizza['massa'] +
 " com os ingredientes:")
for ingrediente in pizza['ingredientes']:
    print("\t" + ingrediente.title())


# Um dicionário dentro de um dicionário
users = {
    'Mateusinho':{
        'first': 'mateus',
        'last': 'fonseca',
        'location': 'sjc'
    },       # não pode esquecer da vírgula separando cada dicionário interno
    'tata': {
        'first': 'tainara',
        'last': 'rayane',
        'location': 'sjc'
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())











