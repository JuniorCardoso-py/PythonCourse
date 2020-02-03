def opçao():
    opcao = ['1','2','3','4','5','6','7']
    n1 = input('\nDigite a opção desejada: ')
    if n1 == '1':
        print('Cadastro de Clientes')
    elif n1 == '2':
        print('Clientes Cadastrados:')
    elif n1 == '3':
        print('Cadastro de Clientes: ')
    elif n1 == '4':
        print('Produtos Cadastrados: ')
    elif n1 == '5':
        print('Vendas')
    elif n1 == '6':
        print('Relatorios de Vendas: ')
    elif n1 == '7':
        print('Sair')
    while n1 not in opcao:
        print('Opção invalida! Digite somente os numeros sugeridos')
        n1 = input('\nDigite a opção desejada: ')
        if n1 == '1':
            print('Cadastro de Clientes')
        elif n1 == '2':
            print('Clientes Cadastrados:')
        elif n1 == '3':
            print('Cadastro de Clientes: ')
        elif n1 == '4':
            print('Produtos Cadastrados: ')
        elif n1 == '5':
            print('Vendas')
        elif n1 == '6':
            print('Relatorios de Vendas: ')
        elif n1 == '7':
            print('Sair')
        