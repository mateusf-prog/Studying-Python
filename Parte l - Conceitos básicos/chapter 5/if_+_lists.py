# 	Mateus 05/01/2023
#
# Verificando itens em uma lista 
ingredientes = ['queijo','presunto','calabresa']
for ingrediente in ingredientes:
	print("Adicionando " + ingrediente.title() + ".")
print("\nTerminamos sua pizza")
print("\n")
#
# faltou presunto na pizzaria 
# Instrução IF dentro do laço for para tratar determinado caso
for ingrediente in ingredientes:
	if ingrediente == 'presunto':
		print("Desculpe, o presunto acabou")
	else:
		print("Adicionando " + ingrediente.title() + ".")
print("\nTerminamos sua pizza")
#
# Verificando listas vazias
ingredientes = []
if ingredientes:
	for ingrediente in ingredientes:
		print("Adicionando " + ingrediente.title() + ".")
else:
	print("\nDesculpe, não temos ingredientes")
print("\n")
#
# Usando mais de uma lista
ingredientes_solicitados = ['presunto','queijo','calabresa','brocolis']
ingredientes_disponiveis = ['presunto','calabresa','brocolis']
for ingredientes_solicitados in ingredientes_solicitados:
	if ingredientes_solicitados in ingredientes_disponiveis:
		print("Adicionando " + ingredientes_solicitados)
	else:
		print("Desculpe, não temos mais " + ingredientes_solicitados)
print("\nTerminamos sua pizza")
