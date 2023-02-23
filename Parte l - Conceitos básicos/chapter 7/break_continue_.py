#   Mateus 09/01/2023
#   Usando break para sair de um laço
prompt = "\nPor favor, digite a cidade que você visitou:"
prompt += "\n(Digite 'quit' para sair.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("A cidade " + city.title() + " é bonita.")
#
#
# Usando continue em um laço
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  
    print(numero)
# Foi usado 'continue' para pular as iterações se os numeros forem pares.
#
# Usando um laço while com listas e dicionários
# Transferindo itens de uma lista para outra
nao_confirmados = ['alice','bob','charlie']
confirmados = []
while nao_confirmados:  # o laço while executa enquanto a lista nao está vazia
    usuario = nao_confirmados.pop()
    print("Verificando usuário: " + usuario.title())
    confirmados.append(usuario)
print("Os seguintes usuários foram confirmados: ")
for confirmado in confirmados:
    print(confirmado.title())
#
#
# Removendo todas as instâncias de valores específicos de uma lista
pets = ['dog','cat','dog','fish','horse','dog']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)
#
#
# Preenchendo um dicionário com dados de entrada do usuário
respostas = {}
enquete_ativa = True
while enquete_ativa:
    nome = input("\nQual seu nome? ")
    resposta = input("Qual montanha você quer conhecer um dia? ")
    respostas[nome] = resposta
    repeat = input("Você gostaria de deixar outra pessoa responder? sim/nao ")
    if repeat == 'nao':
        enquete_ativa = False
    print("--------- RESULTADOS---------")
for nome, resposta in respostas.items():
    print(nome.title() + " quer conhecer a montanha " + resposta.title() + ".")
#
#
