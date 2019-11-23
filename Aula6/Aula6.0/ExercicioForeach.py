# EXERCICIO 3 - Foreach
#  Escreva programa que leia as notas de um aluno
#  Armazene as notas e nomes em listas
#  Imprima:
#       1 - O nome dos alunos e suas respectivas médias e resultados (Aprovado >= 7.0)
#       2 - Média do aluno
#       3 - Resultado (Aprovado >=7.0)

nota = []
alun1 = []
alun2 = []
#alun3 = []
#alun4 = []

alun1.append(input('Digite o nome do Aluno : '))
alun2.append(input('Digite o nome do Aluno : '))
#alun3.append(input('Digite o nome do Aluno : '))
#alun4.append(input('Digite o nome do Aluno : '))

for bla in range(1,5):
    nota.append(float(input(f'Qual as notas do primeiro aluno {bla}? ')))
for bla3 in range(1,5):
    nota.append(float(input(f'Qual as notas do segundo aluno {bla3+1}?  ')))
#for bla4 in range(1,5):
    #nota.append(float(input(f'Qual as notas do terceiro aluno {bla4+1}?')))
#for bla5 in range(1,5):
    #nota.append(float(input(f'Qual as notas do quarto aluno{bla5+1} ?')))
print(f'\n A nota do Aluno 1 é {nota[0,4]} e sua media é : {(nota[0,4]/4)}')
print(f'\n A nota do Aluno 2 é {nota[4,9]} e sua media é : {(nota[0,4]/4)}')
#print(f'\n A nota do Aluno 3 é {Nota[9,14]} e sua media é : {(Nota[0,4]/4)}')
#print(f'\n A nota do Aluno 4 é {Nota[14,19]} e sua media é : {(Nota[0,4]/4)}')


