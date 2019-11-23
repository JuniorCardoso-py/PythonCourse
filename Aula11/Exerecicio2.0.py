# juros = float(input('Qual o valor dos juros ao ano?: '))
# ano = int(input('Qual o periodo em anos de aplicação?: '))
# money = int(input('Qual o valor do investimento?: '))
# juros_2 = juros/100
# calculo_montante = money*(1+juros_2)*ano
# #m=p*(1+i)elevado a numero de meses

# if ano >= 1:
#     print(f'\n O valor investido em {ano} anos é de R${calculo_montante}')
# else:
#     print(f'\n O valor investido em {ano} ano é de R${calculo_montante}')

from metodosExer import juross

juros = float(input('\n Qual o valor dos juros ao ano?: '))
ano = int(input('\n Qual o periodo em anos de aplicação?: '))
money = int(input('\n Qual o valor do investimento?: '))
juros_2 = float(juros/100)


if ano > 1:
    print(f'\n A rentabilidade será de R${juross(juros_2, ano, money)} em {ano} anos')
else:
    print(f'\n A rentabilidade será de R${juross(juros_2, ano, money)} em {ano} ano')
