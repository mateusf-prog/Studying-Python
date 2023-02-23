#   Mateus 11/01/20223
def make_shirt(tamanho, texto = 'Eu amo python'):
    print("O tamanho da camiseta é " + tamanho + " e o texto é " +
    texto.title())
make_shirt('médio')
print("\n\n")
#
#
def describe_city(city, country = 'brasil'):
    print("A cidade de " + city.title() + " fica no " + country.title())
describe_city('pouso alegre')
describe_city('nova yorque', country = 'estados unidos')
print("\n\n")
#
#
def city_country(city, country):
    print(city.title()+ ", " + country.title())
city_country('sjc', 'brasil')
print("\n\n")
#
#
def make_album(cantor, album, faixas = ''):
    m_album = {'cantor': cantor.title(), 'album': album.title(), 'faixas': faixas}
    if faixas:
        m_album = {'cantor': cantor, 'album': album, 'faixas': int(faixas)}
    else:
        m_album = {'cantor': cantor.title(), 'album': album.title()}
    return m_album
dados = make_album('gustavo lima', 'in boston', 24)
print(dados)
dados_2 = make_album('cristiano araujo', 'in the cities')
print(dados_2)
#
#
#   Código corrigido pelo chatGPT
def make_album(cantor, album, faixas = None):
    m_album = {'cantor': cantor.title(), 'album': album.title()}
    if faixas != None:
        m_album['faixas'] = int(faixas)
    return m_album
dados_3 = make_album('ze neto', 'in the roça')
print(dados_3)
dados_4 = make_album('henrique e juliano', 'gandaia', 32)
print(dados_4)
print("\n\n")
#
#
#
def users_album(nome_cantor, nome_album):
    album = {'cantor': nome_cantor.title(), 'album': nome_album.title()}
    return album

ativo = True
while ativo:
        print("--Seu cantor e álbum favorito--")
        print("(Digite 'quit' para sair.)")
        nome_cantor = input("\nDigite o nome do cantor: ")
        if nome_cantor == 'quit':
            break
        nome_album = input("Digite o nome do álbum: ")
        if nome_album == 'quit':
            break
        ativo = False
print(users_album(nome_cantor, nome_album))
#
#

