#   importando uma função específica em um módulo
from new_user import new_user

user = new_user('mateus','fonseca', idade=22)
print(user)
#
#
#   importando uma função em um módulo com um 'alias'(apelido)
from new_user import new_user as nu

user_2 = nu('tainara','rayane', idade=22)
print(user_2)
#
#
#   importando todas as funções de um módulo
from new_user import *
