dados = {}
ativo = True
while ativo:
    nome = input("Diga seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = int(input("Digite seu peso: "))
    altura = int(input("Digite sua altura: "))
    dados[nome] = idade, peso, altura
    pergunta = input("Quer deixar outra pessoas responderem? sim/nao: ")
    if pergunta == 'nao':
        ativo = False
print("-------------RESULTADO-------------")
for nome, dado in dados.items():
    print(nome.title())
    print("\n\tIdade: " + str(dado[0]))
    print("\tPeso: " + str(dado[1]))
    print("\tAltura: " + str(dado[2]))
#
#
lista =[]
program = True
while program:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    pergunta = input("Você deseja parar? s/n ")
    if pergunta == 's':
        break
print("\nA lista é :" + str(lista))
print("O maior número é " + str(max(lista)))
print("O menor número é " + str(min(lista)))



