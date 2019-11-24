#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido 

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
ano_de_nascimento = int(input('Digite o ano de seu nascimento: '))

calc = 2019 - ano_de_nascimento

print(f'\n\tOlá Seja Muito Bem Vindo {nome} {sobrenome} ')


alcool = ['Skol', 'Original', 'Patagonia']
sem_alcool = ['Guaraná','Agua', 'Suco']
if calc >= 18:
    print(f'\nVeja nosso catalogo de produtos: \n\n {alcool[0]} \n {alcool[1]} \n {alcool[2]} \n {sem_alcool[0]} \n {sem_alcool[1]} \n {sem_alcool[2]} ')
else:
    print(f'\nVeja nosso catalogo de produtos: \n\n {sem_alcool[0]} \n {sem_alcool[1]} \n {sem_alcool[2]} ')

sair = (input('\n \n Digite "Sair" para sair do menu: '))
if sair == 'Sair':
    print('\n\tVolte sempre!!!')
