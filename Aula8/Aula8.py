#Aula - 8 -Tuplas 18/11/2019
#Tuplas

Lista =[1,4,6]
Dicionario = {'nome':'user', 'password':'123456'}
Tupla = ('Junior', 'Cardoso', 0, 45.5, Lista, Dicionario)

print(Lista)
print(Dicionario)
print(Tupla)

Lista[1] = 5
Dicionario['password'] = 654321
# ==== Tupla é imutavel ====
lista_pessoas = []
lista_pessoas.append(Tupla)
Tupla[4][1] = 6
print(Tupla[4][1])