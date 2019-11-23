# EXERCICIO 3 - Foreach
#  Escreva programa que leia as notas de um aluno
#  Armazene as notas e nomes em listas
#  Imprima:
#       1 - O nome dos alunos e suas respectivas médias e resultados (Aprovado >= 7.0)
#       2 - Média do aluno
#       3 - Resultado (Aprovado >=7.0)

Nota = []
Alunos = []

for i in range(1,5):
    Alunos.append(input(f'Digite o nome do Aluno {i}: '))
    for a in range(1,5):
        Nota.append(input(f'Digite a nota do Aluno {a}: '))
print


