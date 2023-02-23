# Mateus 29/12/2022
# Ordenando uma lista deforma permanente com o método SORT()
moveis = ['mesa','cadeira','geladeira']
moveis.sort()
print(moveis)
#
abc = ['d','f','l','o','p','b','c','t','p','e','o','u','n']
abc.sort()
print(abc)
#  Ordem alfabética inversa com método reverse=True
abc.sort(reverse=True)
print(abc)
# Lembrando que uma vez alterada dessa forma, não pode mais voltar ao que era
#
# Para manter a forma original da lista pode-se usa o método SORTED()
print(" A ordem da lista original é: " + str(moveis))
print("\nOs móveis em ordem alfabéitca são: ")
print(sorted(moveis))
print("\nA ordem original da lista é: ")
print(moveis)
print(moveis)
#
# Exibir uma lista em ordem inversa com REVERSE()
nomes = ['mateus','sandro','jessica','gabriel','danilo']
print(nomes)
nomes.reverse()
print(nomes)
#
# Descobrir o tamanho de uma lista com LEN()
carros = ['honda','bmw','ferrari','porsche']
print(carros)
print("\nA quantidade de carros é: ")
print(len(carros))
#
#
#		EXERCICIOS
#
#
locais = ['Holanda','Noruega','Espanha','Japão']
print("Meus lugares favoritos são: ")
print(locais)
print("\nMeus países favoritos em ordem alfabética é:")
print(sorted(locais))
print("\nA ordem da lista original é:")
print(locais)
print("\nA lista inversa em ordem alfabética é:")
print(sorted(locais, reverse=True))
print("\nA ordem da lista original é:")
print(locais)
locais.reverse()
print("\nA ordem da lista mudou:")
print(locais)
print("\nA lista voltou a ordem original:")
locais.reverse()
print(locais)
 
