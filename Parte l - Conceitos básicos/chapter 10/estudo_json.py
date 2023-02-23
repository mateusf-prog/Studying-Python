#   Mateus 26/01/2023
#   Usando json.dump() e json.load()

import json

'''numeros = [2, 4, 5, 6, 8, 9]

filename = 'numeros.json'
with open(filename, 'w') as f_obj:
    json.dump(numeros, f_obj)


# Ler a lista de volta para a memória usando json.load()

filename = 'numeros.json'
with open(filename) as f_obj:
    numeros = json.load(f_obj)

print(numeros)
print("\n\n\n\n")'''


# Salvando e lendo dados gerados pelo usuário

'''username = input("Digite seu nome: ")

arquivo = 'username.json'
with open(arquivo, 'w') as f_obj:
    json.dump(username, f_obj)
    print("Bem vindo de volta, " + username.title() + "!")

with open(arquivo) as f_obj:
    nome = json.load(f_obj)
    print("Olá novamente, " + nome.title())'''

# Refatoração

def verificacao_usuario_armazenado():
    '''obtém o nome do usuário já armazenado se estiver disponível'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def saudacoes():
    '''saúda o usuário pelo nome'''
    username = verificacao_usuario_armazenado()
    if username:
        print("Bem vindo de volta, " + username.title())
    else:
        username = input("Qual seu nome? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("Vamos lembrar de você quando você voltar, " + username)

def get_new_username():
    '''pede um novo nome de usuário'''
    username = input("Qual seu nome? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

