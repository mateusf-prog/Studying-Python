#   Mateus 07/01/2023
#   Exercícios
pessoa_1 = {'nome': 'tainara', 'idade': 22, 'local': 'sjc'}
pessoa_2 = {'nome': 'sandro', 'idade': 27, 'local': 'sao paulo'}
pessoa_3 = {'nome': 'mateus', 'idade': 25, 'local': 'sjc'}
pessoas = [pessoa_1, pessoa_2, pessoa_3]
for pessoa in pessoas:
    if pessoa == pessoa_1:
        print(str(pessoa_1['nome'].title()) + " é minha namorada e ela tem " +
        str(pessoa_1['idade']) + " anos de idade!")
    elif pessoa == pessoa_2:
        print(str(pessoa_2['nome'].title()) + " é meu irmão e ele tem " +
        str(pessoa_2['idade']) + " anos de idade!")
    else:
        print(str(pessoa_3['nome'].title()) + " sou eu e tenho " + 
        str(pessoa_3['idade']) + " anos de idade!" + "\n")
#
#
#
maya = {'nome': 'maya', 'raça': 'shitzu', 'dono': 'mateus'}
tipy = {'nome': 'tipy', 'raça': 'shitzu', 'dono': 'suelen'}
mavi = {'nome': 'mavi', 'raça': 'shitzu', 'dono': 'katila'}
pets = [maya, tipy, mavi]
for pet in pets:
    if pet == maya:
        print("O nome do dog é " + maya['nome'].title() + ", sua raça é " +
        maya['raça'].title() + " e seu dono é " + maya['dono'].title())
    elif pet == tipy:
        print("O nome do dog é " + tipy['nome'].title() + ", sua raça é " +
        tipy['raça'].title() + " e seu dono é " + tipy['dono'].title())
    else:
        print("O nome do dog é " + mavi['nome'].title() + ", sua raça é " +
        mavi['raça'].title() + " e seu dono é " + mavi['dono'].title())
#
#
#
num_favoritos = {
    'mateus': 20,
    'tainara': [25, 15],
    'sandro': 7,
    'jessica': 25,
    'maria': [10, 30]
}
for nome, num in num_favoritos.items():
    print ("\nMeu nome é " + nome.title() + " e meu número favorito é " +
    str(num))
#
#
#
cidades = {
    'sjc': {
        'estado': 'sp',
        'população': 725
    },
    'pouso alegre': {
        'estado': 'mg',
        'população': 160
    },
    'rezende': {
        'estado': 'rj',
        'população': 300
    }
}
for cidade, city_info in cidades.items():
    print("\nA cidade é: " + cidade.title())
    estado = city_info['estado']
    info = city_info['população']
    print("\tEstado: " + estado.upper() + "\n\tPopulação: " +
    str(info) + " mil habitantes!")
#
#
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#
#
produtos = {
    'Banana': {
        'preço': 10,
        'estoque': 30
    },
    'Uva': {
        'preço': 7,
        'estoque': 150
    },
    'batata':{
        'preço': 5,
        'estoque': 20
    }
}
for produto, detalhes in produtos.items():
    print ("\nProduto: " + produto.title())
    preço = detalhes['preço']
    estoque = detalhes['estoque']
    print("\tPreço: " + str(preço))
    print("\tEstoque: " + str(estoque))
#
#
alunos = {
    'joao': {
        'nome': 'joao',
        'idade': 20,
        'endereço': 'rua dos bobos, nº 0'
    },
    'maria': {
        'nome': 'maria',
        'idade': 18,
        'endereço': 'rua dos bobos, nº 1'
    },
    'pedro': {
        'nome': 'pedro',
        'idade': 22,
        'endereço': 'rua dos bobos, nº2'
    }
}
for aluno, dados in alunos.items():
    print("\nAluno: " + aluno.title())
    idade = dados['idade']
    nome = dados['nome']
    endereço = dados['endereço']
    print("Nome: " + nome.title())
    print("Idade: " + str(idade))
    print("Endereço: " + endereço.title())
#
#
estudantes = {
    'maria': {
        'nome': 'maria',
        'idade': 15,
        'notas': [8, 10, 15]
    },
    'joao': {
        'nome': 'joao',
        'idade': 20,
        'notas': [10, 7, 22]
    },
    'pedro': {
        'nome': 'pedro',
        'idade': 17,
        'notas': [4, 12, 19]
    }
}
for estudante, ifm in estudantes.items():
    print("\nAluno: " + estudante.title())
    name = ifm['nome']
    age = ifm['idade']
    notas = ifm['notas']
    media = sum(notas) / 3
    print("Nome: " + name.title())
    print("Idade: " + str(age))
    print("Média das notas: " + str(media))
    if media >= 7:
        print("Resultado: Aprovado")
    else:
        print("Resultado: Reprovado")
