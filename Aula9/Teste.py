from metodos import soma, subtração, mutiplicação, divisão_inteira, divisão_fracionada, resto_da_divisão, raiz

print('='*50)
n1 = int(input('\n Digite um numero: '))
n2 = int(input('\n Digite outro numero: '))

# print(f'\n A soma entre {n1} e {n2} é {soma(n1,n2)}')
# print(f'\n A subtração entre {n1} e {n2} é {subtração(n1,n2)}')
# print(f'\n A mutiplciação entre {n1} e {n2} é {mutiplicação(n1,n2)}')
# print(f'\n A divisão_inteira entre {n1} e {n2} é {divisão_inteira(n1,n2)}')
# print(f'\n A divisão_fracionada entre {n1} e {n2} é {divisão_fracionada(n1,n2)}')
# print(f'\n A resto_da_divisão entre {n1} e {n2} é {resto_da_divisão(n1,n2)}')
# print(f'\n A raiz entre {n1} e {n2} é {raiz(n1,n2)}')

print(soma(n1,n2))
print(subtração(n1,n2))
print(mutiplicação(n1,n2))
print(divisão_inteira(n1,n2))
print(divisão_fracionada(n1,n2))
print(resto_da_divisão(n1,n2))
print(raiz(n1, n2))