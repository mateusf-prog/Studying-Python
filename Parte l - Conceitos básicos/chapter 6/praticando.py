produtos = {
    'banana': {
        'nome': 'banana',
        'preço': 3.50,
        'estoque': 232
    },
    'maçã': {
        'nome': 'maçã',
        'preço': 4.70,
        'estoque': 120
    },
    'Pera': {
        'nome': 'pera',
        'preço': 2.35,
        'estoque': 240
    }
}
for produt, key in produtos.items():
    print("Produto: " + produt.title())
    nome = key['nome']
    preço = key['preço']
    estoque = key['estoque']
    valor_estoque = estoque * preço
    print("\nNome: " + nome.title())
    print("Preço: " + str(preço))
    print("Estoque: " + str(estoque))
    print("Valor total em estoque: " + str(valor_estoque))
#
#
itens = {
    'computador': {
        'nome': 'computador',
        'preço': 2500.00,
        'estoque': 10,
        'categorias': ['informática','eletrodomésticos']
    },
    'televisao': {
        'nome': 'televisao',
        'preço': 2750.00,
        'estoque': 23,
        'categorias': 'eletrodomésticos'
    },
    'geladeira': {
        'nome': 'geladeira',
        'preço': 2200.00,
        'estoque': 15,
        'categorias': 'eletrodomésticos'
    },
    'guarda-roupas': {
        'nome': 'guarda-roupas',
        'preço': 1500.00,
        'estoque': 210,
        'categorias': 'móveis'
    },
    'celular': {
        'nome': 'celular',
        'preço': 500.00,
        'estoque': 27,
        'categorias': ['informática','eletroeletrônico']
    }
}
for item, info in itens.items():
    print("\nProduto: " + item.title())
    name = info['nome']
    price = info['preço']
    qtde = info['estoque']
    categorias = info['categorias']
    print("Nome: " + name.title())
    print("Preço: " + str(price))
    print("Categorias: " + str(categorias))
