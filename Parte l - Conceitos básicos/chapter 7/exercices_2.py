# Mateus 09/01/2023
# Exercícios
pedidos_lanches = ['x-bacon','x-salada','x-egg','x-salada',
'x-tudo','x-frango','x-salada',]
pedidos_finalizados = []
active = True
while 'x-salada' in pedidos_lanches:
    pedidos_lanches.remove('x-salada')
    active = False
print("Estamos sem salada no momento")
for pedido in pedidos_lanches:
        print("Preparando seu lanche de " + pedido.title())
while pedidos_lanches:
    lanches = pedidos_lanches.pop()
    pedidos_finalizados.append(lanches)
for lanche in pedidos_finalizados:
    print("Seu " + lanche + " está pronto!")
#
#
respostas = {}
enquete_ativo = True
while enquete_ativo:
    nome = input("\nQual seu nome? ")
    resposta = input("\nSonha em conhecer qual lugar do mundo? ")
    respostas[nome] = resposta
    continuação = input("\nQuer deixar outro usuário responder? sim/nao: ")
    if continuação == 'nao':
        enquete_ativo = False
print("----------RESPOSTAS---------")
for name, resp in respostas.items():
    print(name.title() + " sonha em conhecer " + resp.title())
