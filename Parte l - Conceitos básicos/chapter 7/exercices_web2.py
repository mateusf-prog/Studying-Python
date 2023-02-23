lista = []
program = True
while program:
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)
    pergunta = input("Quer digitar outra palavra? s/n: ")
    if pergunta == 'n':
        break
print("\nAs palavras digitadas em ordem alfabética são " + str(sorted(lista)))
#
#
infos = {}
program = True
while program:
    nome = input("Digite seu nome: ")
    endereço = input("Digite seu endereço: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    infos[nome] = endereço, telefone, email
    pergunta = input("Deseja adicionar mais contatos? s/n: ")
    if pergunta != 's' and pergunta != 'n':
        print("Opção inválida")
    elif pergunta == 'n':
        break
for chave, valor in infos.items():
    print("\nNome: " + chave.title())
    print("Endereço: " + valor[0].title())
    print("Telefone: " + valor[1])
    print("E-mail: " + valor[2])
