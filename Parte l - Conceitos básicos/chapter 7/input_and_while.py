#   Mateus 08/01/2023
#
# Como a função input() trabalha
message = input("Diga-me uma coisa, e eu repetirei de volta para você: ")
print(message)
#
#
name = input("Digite seu nome: ")
print("Olá, " + name.title() + "!")
#
#
# Usando int() para aceitar entradas numéricas
idade = int(input("Qual sua idade? "))
print(idade)
#
#
if idade >= 18:
    print("Você já pode votar!")
else:
    print("Você ainda não tem idade suficiente para votar!")
#
#
# Deixando o usuário decidir quando quer sair
prompt = "\nDiga-me uma coisa e eu repetirei: "
prompt += "\nDigite 'quit' para fechar o programa."
mensagem = ""
while mensagem != 'quit':
    mensagem = input(prompt)
    print(mensagem)
#
#
# Usando um flag para controlar o fluxo de execução de um programa
prompt = "\nDiga-me uma coisa e eu repetirei: "
prompt += "\nDigite 'quit' para fechar o programa."
ativo = True
while ativo:    
    mensagem = input(prompt)
    if mensagem == 'quit':
        ativo = False
    else:
        print(mensagem)