#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe se os qual número é maior ou se os dois são iguais 

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

soma = n1 + n2
multiplicaçao = n1 *n2  
subtraçao = n1 - n2
divisao = n1 / n2

print(f' A soma de {n1} e {n2} é igual a :{soma} \n A multiplicaçao entre {n1} e {n2} é igual a :{multiplicaçao} \n A subtração entre {n1} e {n2} é igual a :{subtraçao} \n A divisão entre {n1} e {n2} é igual a:{divisao} ')
if n1 > n2:
    print('O primeiro número digitado é maior que o segundo.')
elif n1 == n2:
    print('Os dois numeros são iguais.')
else:
    print('O segundo numero é maior que o primeiro.')
