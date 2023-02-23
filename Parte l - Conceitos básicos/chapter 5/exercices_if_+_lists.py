# Mateus 05/01/2023
#
usuarios = ['alberto','mateus','kaio','admin','jessica','rodrigo']
if usuarios:
	for usuario in usuarios:
		if usuario == 'admin':
			print("Olá ADM, saudações!")
		else:
			print("Olá " + usuario.title() + ", seja bem vindo!")
else:
	print("Não há usuários")
print("\n")
#
#
current_users = ['fernando','jessica','bruno','abel','maria','joão']
new_users = ['josé','kaio','jorge','bianca','abel','Fernando']
for new_user in new_users:
	if new_user.lower() in current_users:
		print("Nome " + new_user.title() + " já está em uso.")
	else:
		print("Nome " + new_user.title() + " disponível")
print("\n")
#
#
lista = [1,2,3,4,5,6,7,8]
for num in lista:
	if num == 1:
		print(str(num) + "st")
	elif num == 2:
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "th")
	
