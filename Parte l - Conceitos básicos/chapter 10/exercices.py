#   Mateus 25/01/2023

arquivo = r'C:\Users\mateu\Desktop\python_work\chapter 10\py_working.txt'

'''abrindo o arquivo e armazenando os dados em "dados" e imprimindo'''
'''somente dentro do bloco'''
with open(arquivo) as file_object:
    dados = file_object.read()
    print(dados)


'''abrindo o arquivo e armazenando cada linha dentro do 
arquivo em um lista e imrpimindo essa lista'''
'''somente dentro do bloco'''
with open(arquivo) as object_file:
    for line in object_file.readlines():
        print(line)


'''abrindo o arquivo e armazenando cada linha dentro do arquivo, 
dentro de uma lista e armazenando essa lista dentro de uma variável "lines" '''
'''dessa vez a variável "lines" pode ser trabalhada fora do bloco'''
with open(arquivo) as object_file:
    lines = object_file.readlines()


for line in lines:
    print(line.strip())
print("\n\n\n\n\n")


for line in lines:
    if 'laco' in line:
        print(line.replace('laco', 'NOVO'))
    else:
        print(line)

print("\n\n\n")

'''perguntando ao convidado o seu nome e armazenando seu nome em um arquivo txt'''
convidado = input("Digite seu nome: ")

dado = 'nome_convidado.txt'
with open(dado, 'w') as file_object:
    file_object.write(convidado)

print("\n\n\n")

ativo = True
lista_nomes = []
livro_visitas = 'livro_visitas.txt'

while ativo:
    pessoas = input("Digite seu nome: ")
    lista_nomes.append(pessoas)
    print("Olá " + pessoas.title())
    with open(livro_visitas, 'a') as object_file:
        object_file.write(pessoas.title() + " visitou aqui.\n")
    if len(lista_nomes) == 5:
        ativo = False



    