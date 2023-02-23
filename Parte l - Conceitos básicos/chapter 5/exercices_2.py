#	Mateus 05/01/2023
#	Exercícios
alien_color = 'green'
if 'green' in alien_color:
	print("Você ganhou 5 pontos!")
if 'blue' in alien_color:
	print("Voce perdeu")
#
#
alien_color = 'green'
if alien_color == 'green':
	print("Você ganhou 5 pontos por atingir o alien")
#
# versão com else
if alien_color == 'blue':
	print("Você ganhou 5 pontos")
else:
	print("Você acabou de ganhar 10 pontos")
#
#
alien_color = 'red'
if alien_color == 'blue':
	print("Você ganhou 5 pontos")
elif alien_color == 'black':
	print("Você ganhou 10 pontos")
else:
	print("Você perdeu")
#
#
age = 40
if age < 2:
	print("você é um bebê")
elif age < 4:
	print("Você é uma criança")
elif age < 13:
	print("Você é um garoto")
elif age < 20:
	print("Você é um adolescente")
elif age < 65:
	print("Você é um adulto")
else:
	print("Você é um idoso")
	
	
