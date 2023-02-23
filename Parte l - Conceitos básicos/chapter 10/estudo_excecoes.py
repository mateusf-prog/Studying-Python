#   Mateus 26/01/2023
#   Exceções

# Tratando a exceção ZeroDivisionError
'''forçando o erro'''
#print(5/0)

'''Usando o bloco try-except para tratar a exceção'''
try:
    print(5/0)
except ZeroDivisionError:
    print("Você não pode dividir um número por zero.")


# Usando exceções para evitar falhas

print("Me dê dois núemros e eu os dividirei.")
print("Digite 'q' para sair.")

while True:
    first_number = input("\nPrimeiro número: ")
    if first_number == 'q':
        break
    second_number = input("Segundo número: ")
    if second_number == 'q':
        break
    '''usando o bloco try-except para tratar um possivel erro 
       de divisao por zero'''
    try:
        resposta = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Não pode dividir por zero.")
    else:
        print(resposta)


# Tratando a exceção FileNotFoundError

filename = r'C:\Users\mateu\Desktop\python_work\programando.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except:
    msg = "Desculpe, o arquivo " + filename + " não existe."
    print(msg)
else:
    print(contents)


# Analisando textos

'''o método split() separa uma string em partes sempre que encontra
 um espaço, e armazena tocdas as partes em uma lista'''

titulo = "Cartas de inglaterra"
print(titulo.split())

arquivo = r'C:\Users\mateu\Desktop\python_work\cartas_de_inglaterra.txt'

try:
    with open(arquivo, encoding="utf-8") as f_obj:
        conteudo = f_obj.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    palavras = conteudo.split()
    num_palavras = len(palavras)
    print("O arquivo " + arquivo + " tem " + str(num_palavras) + 
    " palavras.")

