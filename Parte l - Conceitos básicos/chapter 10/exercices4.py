#   Mateus 29/01/2023

import json

def verificacao_de_existencia():
    '''verifica a existência do arquivo .json'''
    arquivo = 'favorite_number.json'
    try:
        with open(arquivo) as f_obj:
            conteudo = json.load(f_obj)
    except FileNotFoundError:
        None
    else:
        return conteudo

def imprimir_numero():
    '''imprime o numero favorito e se nao existir, ele cria um arquivo .json'''
    arquivo = 'favorite_number.json'
    if verificacao_de_existencia():
        with open(arquivo) as f_obj:
            conteudo = json.load(f_obj)
            print(f"Seu numero favorito é {conteudo}")
    else:
        number = input("Digite seu numero favorito: ")
        with open(arquivo, "w") as f_obj:
            json.dump(number, f_obj)

imprimir_numero()




