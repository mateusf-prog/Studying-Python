# Mateus 05/01/2023
#
lista = [1,2,3,4,5,6,7]
for num in lista:
	if num % 2 == 0:
		print("O número " + str(num) + " é par")
	else:
		print("O número " + str(num) + " é ímpar")
print("\n")
#
#
palavras = ['boneco','uva','tela','mesa','computador','cpu','cadeira']
for palavra in palavras:
	if len(palavra) > 5:
		print("A palavra " + palavra + " tem mais de 5 letras")
	else:
		print("A palavra " + palavra + " tem MENOS de 5 letras")
print("\n")
#
#
nomes = ['tainara','ana','carolina','joana','otavio']
for nome in nomes:
	if nome[0] == nome[-1]:
		print("O nome " + nome.title() + " começa e termina com a mesma letra")
	else:
		print("O nome " + nome.title() + " é normal")
print("\n")
#
#
peso = 63
altura = 1.80
imc = peso / (altura**2)
if imc < 18.5:
	print("Abaixo do peso")
elif imc < 24.9:
	print("Peso normal")
elif imc < 29.9:
	print("Sobrepeso")
else:
	print("Obesidade")
print("\n")

#
#
nome = 'ana'
idade = 20
if len(nome) < 4:
	print("Seu nome é curto")
elif len(nome) < 6=:
	print("Nome normal")
elif len(nome) > 6:
	print("Seu nome é longo")
if idade < 18:
	print("Você é jovem")
elif idade < 60:
	print("Você é adulto")
else:
	print("Você é idoso")
