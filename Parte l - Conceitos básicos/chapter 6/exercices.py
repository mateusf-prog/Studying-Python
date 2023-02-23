#   Mateus 06/01/2023
#   Exercícios
usuario = {'nome': 'tainara', 'sobrenome': 'pereira', 'idade': 22, 'cidade': 'zoro'}
print("O nome é: " + usuario['nome'].title() )
print("O sobrenome é: " + usuario['sobrenome'].title())
print("A idade é: " + str(usuario['idade']))
print("A cidade é: " + usuario['cidade'].title())
print("\n")
#
#
num_favoritos = {'mateus': 20, 'tainara': 10, 'sandro': 7, 'jessica': 25,'maria': 5,}
for key, value in num_favoritos.items():
    print("\nO número favorito de " + key.title() + " é " + str(value))
#
#
rios = {'minas gerais': 'sapucaí','acre': 'amazonas', 'são paulo': 'paraíba',}
for state, rio in rios.items():
    print("\nNo estado " + state.title() + " passa o rio " + rio.title() + "!")
for rio in rios.values():
    print(rio.title())
for state in rios.keys():
    print(state.title())
print("\n")
#
#
favorite_languages = {
    'jen': 'python',
    'sarah': 'c#',
    'edward':'ruby',
    'phil': 'python',
    }
nomes = ['jen','sarah','edward','phil','maria','joao','clovis']
for nome in nomes:
    if nome in favorite_languages.keys():
        print("\nOlá " + nome.title() + ", obrigado por paticipar da pesquisa!")
    else:
        print("\nOlá " + nome.title() + ", você quer participar da pesquisa?")