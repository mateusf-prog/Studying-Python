#   Mateus 12/01/2023
#
#   Passando uma lista para uma função
def saudações(nomes):
    for nome in nomes:
        msg = "Olá, " + nome.title() + "!"
        print(msg)

lista_nomes = ['ana','eduardo','pedro']
#
#
#   Modificando uma lista em uma função
def print_models(nao_terminados, terminados):
    while nao_terminados:
        transferencia = nao_terminados.pop()
        print("Imprimindo modelo: " + transferencia.title())
        terminados.append(transferencia)

def mostrar_terminados(terminados):
    for terminado in terminados:
        print(terminado.title())

nao_concluido = ['caixa iphone','caixa','samsung','banner asus']
concluido = []

print_models(nao_concluido[:], concluido)
mostrar_terminados(concluido)
print(nao_concluido)
#
#
#   Evitando que uma função modificque uma lista
# A notação de fatia [:] cria uma cópia da lista para ser enviada à função.
print_models(nao_concluido[:])