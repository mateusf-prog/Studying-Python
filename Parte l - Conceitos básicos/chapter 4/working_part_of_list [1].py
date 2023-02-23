# Mateus 02/01/2023
# Fatiando uma lista
# para acessar o item da posição 0 e 1 da lista
players = ['Mateus','Sandro','Danilo','Gabriel','Marcos','Jessica']
print(players[0:2]) 
#
#
# Sem um índice de início, Python usa o início da lista
print(players[:3])
#
#
# Se quisermos apresentar os três últimos jogadores da lista, podemos usar a fatia
print(players[-3:])
#
#
# Percorrendo uma fatia com um laço
print("\nEsses são os 3 primeiros jogadores: ")
for player in players[:3]:
	print(player.title())
#
#
# Copiando listas
my_players = players[:]
print(my_players)
# Copiou todos os itens da lista players para a lista my_players
#
# Isso não funciona
my_players = players
