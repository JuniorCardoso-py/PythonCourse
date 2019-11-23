# 2
# Mercado Tech
# Solicitar nome do funcionario
# Solictar Idade
# Informar se funcionario pode adquirir pordutos alcoolicos

print('='*50)

print ('\t ========MERCADO TECH========')

print('='*50)

nome = input('\n Qual o seu nome? ')
idade = int(input('\n Qual sua idade? '))

if idade >= 18:
    print('Pode adquirir qualquer produto disponivel do Mercado Tech!')
else:
    print('Infelizmente alguem não vai ficar só no suquinho')
