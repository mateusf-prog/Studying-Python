def contar_palavras(arquivo):
    '''conta o número aproximado de palavras em um arquivo'''
    try:
        with open(arquivo, encoding="utf-8") as file_object:
            conteudo = file_object.read()
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        palavras = conteudo.split()
        num_palavras = len(palavras)
        print("O número de palavras contida no arquivo " +
        arquivo + " é de " + str(num_palavras) + " palavras.")

