print('\t \nCalculo de investimento')
ano = int(input('\nQuantos anos faltam para o vencimento do titulo?: '))
n1 = int(input('\nQual a porcentagem desejada para investir no tesouro Selic: '))
while n1 < 10:
    print('Porcentagem minima de 10% digite novamente a porcentagem a ser investida: ')
    n1 = int(input('\nQual a porcentagem desejada para investir no tesouro Selic: '))
porc_selic = 10410*(n1/100)
tesouro_selic = float(5.02/100)
total_anos = porc_selic*tesouro_selic
toto = total_anos*tesouro_selic
perg = input(f'\n O valor de investimento é R${porc_selic}, está de acordo?: [N/Y]:  ')
while perg == ('N', 'n'):
    ano = int(input('\nQuantos anos faltam para o vencimento do titulo?: '))
    n1 = int(input('\nQual a porcentagem desejada para investir no tesouro Selic: '))
    perg = input(f'\n O valor de investimento é R${porc_selic}, está de acordo?: [N/Y]:  ')
if perg == ('Y', 'y'):
    print(f'O valor para ser retirado em {ano} anos é de {toto} ')