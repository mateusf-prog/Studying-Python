#   Mateus 17/01/2023
#   Passando um número arbitrário de argumentos
#   Python cria uma tupla e armazena os valores recebidos   
def make_pizza(*toppings):
    '''imprime os ingredientes de uma pizza'''
    print(toppings)

make_pizza('pepperoni')
make_pizza('presunto','calabresa','queijo')
#
#
#   Misturando argumentos posicionais e arbitrários
def make_pizza2(size, *toppings):
    '''Apresenta a pizza que estamos prestes a preparar'''
    print("\nPizza tamanho " + str(size) + " com os ingredientes: ")
    for topping in toppings:
        print("- " + topping)

make_pizza2(24, 'calabresa')
make_pizza2(32, 'calabresa','presunto','cebola')
#   python armazena o primeiro valor no parâmetro 'size' e os demais 
#   na tupla 'toppings'
#
#
#   Usando argumentos nomeados e arbitrários
# Os asteriscos duplos antes do parâmetro **user_info fazem
# Python criar um dicionário vazio chamado user_info e colocar quaisquer
# pares nome-valor recebidos nesse dicionário
def build_profile(first, last, **user_info):
    '''Constrói um dicionário contendo tudo o que sabemos sobre o usuário'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', 
field='physics')
print(user_profile)
#
#
#

