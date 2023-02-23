#   Mateus 26/01/2023

ativo = True

print("---Soma de dois numeros informados---")
while ativo:
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
    except ValueError:
        pass
    else:
        res = num1 + num2
        print("O resultado é " + str(res))
        break



arquivo1 = r'C:\Users\mateu\Desktop\python_work\gatos.txt'
arquivo2 = r'C:\Users\mateu\Desktop\python_work\cachorros.txt'
lista = [arquivo1, arquivo2]

for item in lista:
    try:
        with open(item) as file_onject:
            conteudo = file_onject.read()
    except FileNotFoundError:
        print("Arquivo " + item + " não encontrado.")
    else:
        print(conteudo.title())
