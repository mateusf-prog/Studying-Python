#   Mateus 24/01/2023

'''Lendo um arquivo inteiro e armazenando em uma variável'''
filename = r'C:\Users\mateu\Desktop\python_work\chapter 10\numeros_pi.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


'''o método readlines() armazena cada linha do arquivo em uma 
lista e essa lista é armazenada em lines'''
with open(filename) as file_object:
    lines = file_object.readlines()


'''usando laço for para percorrer cada linha do arquivo'''
'''cada linha de 'lines' corresponde a cada linha do arquivo'''
for line in lines:
    print(line.rstrip())


'''criando  uma string contendo todos os digitos do arquivo'''
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# Escrevendo dados em um arquivo vazio

arquivo1 = 'programando.txt'
''' "a" modo concatenação -- "r" modo leitura -- "w" modo escrita "'''
with open(arquivo1, 'a') as file_object:
    file_object.write("Eu gosto de programar.\n")
    file_object.write("Eu gosto de python.\n")






