import json

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

saudacoes()