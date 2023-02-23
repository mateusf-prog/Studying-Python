# Mateus 29/12/2022
# Usando a função range()
for value in range(1, 10):
	print(value)
#
#
#
# Usando range() paracriar umalista de números
numbers = list(range(1,30,5))
print(numbers)
# nesse caso a contagem começa no 1 até o 30 sendo somando de 5 em 5
#
#
#
quadrados = []
for value in range(1,12):		# pedimos ao python para percorrer esse range de 1,11
	quadrado = value**2			# o valor é elevado ao quadrado e armazenado na variável quadrado
	quadrados.append(quadrado) 	# cada novo valor em quadrado é concatenado a lista quadrados
print(quadrados)
#
#
#
# Estatísticas simples comumalista de números
digits = [1,2,3,4,5,6]
min(digits)		# valor mínimo da lista
max(digits)		# valor máximo da lista
sum(digits)		# soma da lista
#
#
#
# Lista comprehensions
# Uma lista comprehensions permite gerar a mesma lista anterios com apenas uma linha de código
squares = [value**2 for value in range(1,12)]
print(squares)
