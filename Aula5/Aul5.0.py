#3 -
# Cadastro Produtos Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do porduto ( Alcoolicos e não alcoolicos)
# Exibir o produto cadastrado

print('Cadastre 3 Produtos!!')
print('Categoria 1 para alcool e 2 para sem alcool')

pr1 = input('Cadastre o nome do produto aqui : ')
pr11 = int(input('E a categoria ? )')
while pr11 < 1 or > 2:
    print('Dado informado incorreto, Digite novamente!')
    if pr11 == 1:
        print('Alcoolico')
    elif pr11 == 2:
        print('Não Alcoolico')

print(f' \n O produto Cadastrado é {pr1} e sua categoria é {pr11}.')
