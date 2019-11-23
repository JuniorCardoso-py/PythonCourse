# Aula 4
#Fazer um programa que leia 2 numeros
#Realize as 4 operações matematicas
#Imprima o resultado das operações
#Diga Qual numero é o maior dos dois numeros

n1= int(input('Diga um numero:'))
n2= int(input('Diga outro numero:'))
Soma = n1+n2
Multiplicação = n1*n2
Subtração = n1-n2
Divisão =n1/n2

print('A soma desses numeros é: {} \n \t A multiplicação é: {}\n \t\t A subtração é: {}\n \t\t\t E a Divisão é: {:.2} \n '.format(Soma,Multiplicação,Subtração,Divisão))

if n1 > n2:
    print('O primeiro numero é maior que o segundo')
elif n2 > n1:
    print ('O segundo numero é maior que o primeiro')
else:
    print('Os numeros são iguais')
