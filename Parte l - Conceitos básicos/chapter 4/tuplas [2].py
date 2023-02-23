# Mateus 02/01/2023
# 
# Tuplas - As tuplas são parecidas com listas, porém não podem ser modificadas 
# e são acompanhadas de colchetes ao invés de chaves
#
dimensions = (200, 120)
print(dimensions)		# imprime (200, 20)
print(dimensions[1])		# imprime 120
print("\n")
#
# 
# Percorrendo todos os valores de uma tupla com um laço
alturas = (10,120)
for altura in alturas:
	print(altura)
print("\n")
#
#
# podemos atribuir um novo valor a uma variável que armazena uma tupla
print ("Alturas originais: ")
for altura in alturas:
	print(altura)
alturas = (20, 80)
print ("\nAs novas alturas são: ")
for altura in alturas:
	print(altura)
