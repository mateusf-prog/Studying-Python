ativo = True
while ativo == True:
    pessoa = input("\nDigite sua idade: ")
    if pessoa == 'quit':
        break
    pessoa = int(pessoa)
    if pessoa <= 3:
        print("\nO ingresso é gratuito")
    elif pessoa <12:
        print("\nO ingresso custa 10$")
    else:
        print("O ingresso custa 15$.")
    active = False