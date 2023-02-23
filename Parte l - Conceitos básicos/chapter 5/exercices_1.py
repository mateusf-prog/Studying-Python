car = 'audi'
if car == 'audi':
	print ("é o mesmo carro")
else:
	print("não é o mesmo \n")
#
#
numeros = [1,2,3,4,5]
numeros_2 = [3,1,5,6,7,8]
if numeros >= numeros_2:
	print ("a lista é maior")
else:
	print("a lista não é maior")
#
#
inteiros = [10,40,20,70]
print(10 in inteiros)		# está
print(5 in inteiros)		# está
print(5 not in inteiros)	# não está
#
#
idade = 19
idade_2 = 20
if idade > 20:
	if idade > idade_2:
		print("A idade 1 é maior que a idade 2")
	else:
		print("A idade 1 NÃO é maior que a idade 2")
else:
	print("A idade 2 é maior que a idade 1")
#
#
cor = 'Amarela'
print(cor == 'amarela')			# imprime False
print(cor.lower() == 'amarela')	# imrpime True
