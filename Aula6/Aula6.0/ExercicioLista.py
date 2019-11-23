# EXERCICIO 1 - LISTAS
#  Escreva programa que leia o nome de 10 alunos
#  Armazene os nomes em uma lista
#  Imprima a lista

lista = []

for i in range(1,11):
    lista.append(input(f'Escreva o nome do aluno {i} : '))
print(lista)