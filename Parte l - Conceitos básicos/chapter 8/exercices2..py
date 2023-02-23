#   Mateus 16/01/2023
def mostrar_itens(lista):
    for item in lista:
        print(item.title())

magicos = ['bob','julie','charlie','steve']
mostrar_itens(magicos)
print("\n")
#
#
def make_great(lista):
    for item in lista:
        item = 'o grande ' + item
        print(item.title())
make_great(magicos)
print(magicos)


def make_great(lista):
    for i in range(len(lista)):
        lista[i] = "o Grande " + lista[i]
    return lista

print(make_great(magicos))
