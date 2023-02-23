#		EXERCÍCIOS
#
cars = ['bmw','porsche','mercedes','audi','cadillac']
print("A lista de carros é: \n" + str(cars))
print("\nOs três primeiros da lista são: ")
print(cars[:3])
print("\nOs três itens do meio da lista são: ")
print(cars[1:4])
print("\nOs três últimos itens da lista são: ")
print(cars[-3:])
print("\n")
print("\n")
#
#
pizzas = ['pepperone','mussarela','calabresa','presunto']
friend_pizzas = pizzas[:]
pizzas.append('portuguesa')
friend_pizzas.append('bacon')
print("Minhas pizzas preferidas são: ")
for pizza in pizzas[:]:
	print(pizza.title())
print("\nAs pizzas favoritas de meu amigo são: ")
for pizza_friend in friend_pizzas[:]:
	print(pizza_friend.title())
