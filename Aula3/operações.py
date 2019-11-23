nome = input('Digite seu nome: ')
print (nome)

sobrenome = input('Digite seu sobrenome: ')
print('Seu nome completo é: ','\t', nome, sobrenome)

idade = int(input('Quantos anos você tem? '))
print("$"*50, '\n')
print(f'Seu nome é {nome} {sobrenome} e você tem {idade} anos de idade.')
print('\n', "$"*50, sep='')
print('\n')
if idade < 23: 
    print('Não pode usar mercado Tech, para o que presta')
    breakpoint
if idade > 18: 
    print('Tamo Junto!! Partiu Mercado TECH. ')
    breakpoint
if idade == 18:
    print('Bora bebe !')
    breakpoint

# OU ASSIM
#if idade >= 18:
    #print('Tamo Junto!! Partiu Mercado TECH. ')
   # breakpoint

