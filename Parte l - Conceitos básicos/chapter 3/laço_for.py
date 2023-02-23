# Mateus 29/12/2022
# Percorrendo uma lista com laço FOR
cores = ['preto','branco','marrrom','azul']
for cor in cores:
	print(cor)
# Quando usar laços pela primeira vez, tenha em mente que o conjunto de
# passos será repetido, uma vez para cada item da lista, não importa quantos
# itens haja na lista.
print("\n")
#
# Exibindo uma mensagem para cada item da lista
cores = ['preto','branco','marrrom','azul']
for cor in cores:
	print(cor.title() + ", é uma cor bonita!")
	print("Eu gosto da cor " + cor.title() +"\n")
print("\nTodas as cores são bonitas!")
print("\n")
# Exibindo uma mensagem final apenas uma vez, já que está fora da intendação
#
#       EXERCÍCIOS
pizzas = ['calabresa','portuguesa','americana']
for pizza in pizzas:
	print(pizza.title())
	print("Gosto de pizza de " + pizza.title() + "\n")
print("\nEu realmente amo pizzas! \n \n \n \n")
#
#
animals = ['dog','cat','horse']
for animal in animals:
	print("Eu queria ter um " + animal.title() + "\n")
print("Qualquer animal desses seria uma ótima companhia! \n")
