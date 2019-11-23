#--- Exercicio 4  - Impressão de dados com a função Input
#--- Crie a tela inicial para um sistema de compra de bebidas 
#--- A tela deve conter cabeçalho, menu, tela de boas vindas e rodapé
print('$'*50)
print('\n\tBem vindo ao sistema de compras Online\n')
print('$'*50)

n1 = []

boas_vindas = input('\nVocê deseja realizar alguma compra hoje [Sim/Não] ?:  ')
resS = 'Sim'
resN = 'Não'
if boas_vindas == resS:
    print('Certo!! Selecione no menu o que deseja.')
    n2 = []
    for a in range(0,1):
        n2.append(input('\nDeseja comprar bebidas alcoolicas digite: [Sim/Não]'))
        if n2[0] == resS:
            print('Aqui estão nossos produtos disponiveis: \nSkol R$ 1,89 \nOriginal R$2,90 \nPatagonia R$3,50')
            break
        elif n2[0] ==resN:
            print('Continue com o menu')
        n2.append(input('Deseja comprar bebidas não alcoolicas digite: [Sim/Não]'))
        if n2[1] == resS:
            print('Aqui estão nossos produtos disponíveis: \nSuco R$ 1,89 \nFanta R$2,90 \nGuaraná R$3,50')
            break
        elif n2[1] == resN:
            print('Continue com o menu')
        n2.append(input('Deseja somente olhar o nosso menu de produtos e preços digite: [Sim/Não]'))
        if n2[2] == resS:
            print('Aqui estão todos nossos produtos\n\t BEBIDAS ALCOOLICAS \nSkol R$ 1,89 \nOriginal R$2,90 \nPatagonia R$3,50\nSuco R$ 1,89 \Fanta R$2,90 \nGuaraná R$3,50')
            break
if boas_vindas == resN:
    print('\nTudo bem volte sempre!!')

rodape = '\n                                                                  HBSIS LOVE YOU =]'
print(f'{rodape}')