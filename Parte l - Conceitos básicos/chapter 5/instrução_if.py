#	Mateus 03/01/2023
#
#	Intrução if
cars = ['audi','bmw','mercedes','porsche']
for car in cars:
	if car == 'bmw': 
		print(car.upper())
	else:
		print(car.title())
print("\n")
#
#
# Teste de condição - True ou False
carro = 'bmw'
carro == 'bmw'
# imprime True
#
#
# O teste de condição diferencia letras maiúsculas de minúsculas
carro_1 = 'Audi'
carro_1 == 'audi'
# imprime False
#
#
# convertendo o valor para letras minúsculas antes de fazer a comparação
carro_1.lower() == 'audi'
# imprime True
#
# Verificando a diferença
ingredientes = 'queijo'
if ingredientes != 'presunto':		# != (difetente de)
	print("Não tem")
else:
	print("Tem")
print("\n")
#
#
idade = 25
if idade != 18:
	print("sua idade não é 18 anos! \n")
else:
	print("sua idade é 18 anos!")
print("\n")
#
