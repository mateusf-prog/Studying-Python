# Mateus 28/12/2022 - Listas
#
nomes = ['Mateus',' Sandro','Jessica','Danilo','Gabriel']
print(nomes[1].strip()) #mostre o item 2 da lista sem espaços em branco
print(nomes[2]) #mostre o item 3 da lista 
print(nomes[-1]) # -1 mostra sempre o ultimo item de uma lista e por ai vai
message = "Meu irmão mais velho é: " + nomes[2].upper() 
print(message)
print("\n")
#
#
# Trocando o item 1 que era "Sandro" para o novo item 
nomes[1] = 'Vaneide' #trocou o item 1 que era "Sandro" para o novo item 
print(nomes)
print("\n")
#
#
# Concatenando novos itens ao final da lista
nomes.append('Marcos')
print(nomes[5])
print(nomes)
print("\n")
#
#
#
mouses = []
print(mouses)
mouses.append('razer')
mouses.append('logitech')
mouses.append('redragon')
print(mouses)
print("\n")
#
#
# Inserindo elementos a uma lista
mouses.insert(0, 'hyperx')
print(mouses)
print("\n")
#
# Removendo um item usando instrução DEL
comodo = ['sala','cozinha','banheiro','quarto']
del comodo[2] #removendo o item da posição 2
print(comodo)
print("\n")
# 
# Removendo um item com método POP
roupas = ['calças','camisas','shorts']
print(roupas)
# Removendo o último item da lista com pop() e armazenando em uma nova variável
popped_roupas = roupas.pop()
print("Itens removidos: " + popped_roupas)
print("Itens que sobraram: " + str(roupas))
# Convertendo a lista em string para exibir em uma frase 
print("Nova Lista: " + str(roupas)) 
print("\n")
#
# Removendo um item de acordo com um valor - método REMOVE
#  Às vezes, você não saberá a posição do valor que quer remover de uma
#  lista sendo assim o método remove() poderá ser usado.
cores = ['preto','branco','azul','amarelo']
print(cores)
cores.remove('branco')
print(cores)
#
