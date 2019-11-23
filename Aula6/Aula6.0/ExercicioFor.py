# EXERCICIO 2 - For
#   Escreva programa que leia o numero inteiro
#   Calcule a tabuada do numero informado 
#   Imprima a tabuada com a conta

numero = int(input('Digite um numero: '))
for i in range(0,10+1):
    print(f'{i} x {numero} = {i*numero} ')