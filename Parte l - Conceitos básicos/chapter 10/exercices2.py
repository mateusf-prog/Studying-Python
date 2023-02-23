respostas = 'respostas.txt'
count = 0

while True:
    resposta = input("Porque você gosta de programação? \n")
    if len(resposta) == 0:
        continue
    else:
        with open(respostas, 'a') as object_file:
            object_file.write(resposta + "\n")
        count += 1
    if count == 3:
        break


