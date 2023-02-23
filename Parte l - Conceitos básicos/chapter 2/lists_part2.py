# Removendo um item de acordo com o valor
peças = ['motherboard','ram','ssd','fonte']
print(peças)
# Armazenamos o valor ducati em uma nova variável
not_using = 'motherboard'
# Usamos essa variável para dizer ao python qual valor deve ser removido da lista
peças.remove(not_using)
print(peças)
# O valor 'motherboard' foi removido da lista inical mas continua
# armazenado em na variável not_using
print("\nA " + not_using.title() + " não está sendo mais usada.")
#
#
#
#
#		EXERCÍCIOS
#
convidados = ['Fernanda','Rubia','Mara']
print("Olá, " + convidados[0] + " quero te convidar para o meu jantar.")
print("Olá, " + convidados[1] + " quero que você vá ao meu jantar.")
print("Olá, " + convidados[2] + " gostaria que viesse em meu jantar.")
#
#
convidadados_ausentes = 'Rubia'
convidados.remove('Rubia')
convidados.insert(1, 'Eloisa')
#print("A nova lista de convidados é: " + str(convidados))
#
print ("\nOlá, " + convidados[0] + " quero que venha ao meu jantar.")
print ("Olá, " + convidados[1] + " gostaria que viesse ao meu jantar.")
print ("Olá, " + convidados[2] + " venha ao meu jantar hoje.")
print("\nA " + convidadados_ausentes + " não irá comparecer.")
#
#
convidados.insert(0, 'Joana')
convidados.insert(3, 'Maya')
convidados.append('Mel')
print("\nOlá, " + convidados[0] + ", " + convidados[3] + " e " + convidados[-1] + " quero que venham ao meu jantar.")
print("\nA lista de convidados atualizada é: " + str(convidados))
print("\nDesculpe, gente. Pois terei que remover alguns convidados.")
convidados_removido1 = convidados.pop(0)
print("\nDesculpe " + convidados_removido1 + " você foi removido.")
convidados_removido2 = convidados.pop(0)
print("\nDesculpe " + convidados_removido2 + " você foi removido.")
convidados_removido3 = convidados.pop(0)
print("\nDesculpe " + convidados_removido3 + " você foi removido.")
convidados_removido4 = convidados.pop(0)
print("\nDesculpe " + convidados_removido4 + " você foi removido.")
print("\nOlá, " + convidados[0] + " você ainda está na lista!")
print("\nOlá, " + convidados[1] + " você ainda está na lista!")
print("\nA lista de convidados atualizada é: " + str(convidados))
del convidados[0]
del convidados[0]
print("\nA lista de convidados atualizada é: " + str(convidados))



