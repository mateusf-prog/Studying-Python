#		ECERCÍCIOS
#
pratos = ('arroz', 'feijão', 'macarrão', 'frango', 'purê')
print("Os pratos oferecidos no restaurante são: ")
for prato in pratos:
	print(prato.title())

# forçando um erro
#pratos[0] = 'carne'
# TypeError: 'tuple' object does not support item assignment
#
print("\n")
pratos = ('arroz', 'feijão', 'macarrão', 'carne','batata')
print("Os novos pratos são: ")
for prato in pratos:
	print(prato.title())
