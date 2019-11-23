#Crie um programa que leia 4 notas
#Imprima a maior nota
#Imprima a menor nota
# Imprima a média
#Imprima se o aluno foi aprovado ou reprovado (media 7.0)

nota1 = int(float(input('Qual a Primeira nota? '))) 
nota2 = int(float(input('Qual a Segunda nota? ')))
nota3 = int(float(input('Qual a Terceira nota? ')))
nota4 = int(float(input('Qual a Quarta nota? ')))
media = int(float(nota1 + nota2 + nota3 + nota4))
mediafin = media / 4


print(f' \n Suas Notas foram {nota1} {nota2} {nota3} {nota4} \n ')
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    print(f'Parabéns sua maior nota foi {nota1} \n ')
if nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    print(f'Parabéns sua maior nota foi {nota2} \n ')
if nota3 > nota2 and nota3 > nota1 and nota3 > nota4:
    print(f'Parabéns sua maior nota foi {nota3} \n ')
if nota4 > nota2 and nota4 > nota3 and nota4 > nota1:
    print(f'Parabéns sua maior nota foi {nota4} \n ')
elif nota1 and nota2 and nota3 and nota4 == nota1 and nota2 and nota3 and nota4:
    print('Suas notas são iguais \n ')
if nota1 < 7:
    print(f'Nossa que horror! {nota1} \n ')
if nota2 < 7:
    print(f'Nossa que horror! {nota2} \n ')
if nota3 < 7:
    print(f'Nossa que horror! {nota3} \n ')
if nota4 < 7:
    print(f'Nossa que horror! {nota4} \n ')
elif nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    print(f' \n {nota1} Essa foi sua pior nota!!! \n ')  
    breakpoint
if nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    print(f' \n {nota2} Essa foi sua pior nota!!! \n ')
    breakpoint
if nota3 < nota2 and nota3 < nota1 and nota3 < nota4:
    print(f' \n {nota3} Essa foi sua pior nota!!! \n ')
    breakpoint
if nota4 < nota2 and nota4 < nota3 and nota4 < nota3:
    print(f' \n {nota4} Essa foi sua pior nota!!! \n ')
    breakpoint
    

print(f'A sua média é {mediafin}')

if mediafin > 7:
    print('Aprovadoooooo \n')
else:
    print(' \n Tenta de novo Nubão, REPROVADO \n')