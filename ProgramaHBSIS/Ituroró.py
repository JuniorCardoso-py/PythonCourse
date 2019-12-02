# 1 - O programa deve ter um menu interativo com cabeçalho,local para:
# Cadastro de clientes
# ver clientes cadastrados, cadastro de produtos, ver produtos
# cadastrados, venda de produtos
# relatórios de vendas e a opção sair.
# Este menu deve se repetir até que a opção sair for chamada.
menu2 ='''Bem Vindo ao Menu Principal !

 1 - Cadastro de Cliente
 2 - Ver Clientes Cadastrados
 3 - Cadastro de Produtos
 4 - Ver Produtos Cadastrados
 5 - Vendas
 6 - Relatórios de Vendas
 7 - Sair '''
menu ='''
##################################################################################
#                       Festival de Cerveja em Ituroró                           #
##################################################################################

Bem Vindo ao Menu Principal !

 1 - Cadastro de Cliente
 2 - Ver Clientes Cadastrados
 3 - Cadastro de Produtos
 4 - Ver Produtos Cadastrados
 5 - Vendas
 6 - Relatórios de Vendas
 7 - Sair '''

opcao = ['1','2','3','4','5','6','7']
print(menu)
n1 = input('\nDigite a opção desejada: ')
if n1 == '1':
    print('Cadastro de Clientes')
    cadastro = input('Digite o nome do cliente: ')
    codigo = []
    codigo.append(cadastro)
    resS = ['S','s']
    resN = ['N','n']
    perg = input('Deseja cadastra mais algum cliente: [S/N] ')
    if perg in resS:
        cadastro = input('Digite o nome do cliente: ')
        codigo.append(cadastro)
        resS = ['S','s']
        resN = ['N','n']
        perg = input('Deseja cadastrar mais algum cliente: ')
    elif perg in resN:
        pperg = input('Se deseja continuar com menu digite S, se deseja sair e voltar ao menu principal digite Sair: ')
        if pperg in resS:
            print(menu2)
            n1 = input('\nDigite a opção desejada: ')
        if n1 == '1':
            print('Cadastro de Clientes')
            cadastro = input('Digite o nome do cliente: ')
            codigo = []
            codigo.append(cadastro)
            resS = ['S','s']
            resN = ['N','n']
            perg = input('Deseja cadastra mais algum cliente: [S/N] ')
        if perg in resS:
            cadastro = input('Digite o nome do cliente: ')
            codigo.append(cadastro)
            resS = ['S','s']
            resN = ['N','n']
            perg = input('Deseja cadastrar mais algum cliente: ')
        elif perg in resN:
            pperg = input('Se deseja continuar com menu digite S, se deseja sair e voltar ao menu principal digite Sair: ')
        if pperg in resS:
            print(menu2)
            n1 = input('\nDigite a opção desejada: ')       
    elif n1 == '2':
        print('Clientes Cadastrados: ')
        for c in cadastro:
            print(cadastro)
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
            if n1 == '1':
                cadastro = input('Digite o nome do cliente: ')
                codigo = []
                codigo.append(cadastro)
                resS = 'S','s'
                resN = 'N','n'
                perg = input('Deseja cadastrar mais algum cliente: [S/N] ')
        while perg == resS:
            cadastro = input('Digite o nome do cliente: ')
            codigo.append(cadastro)
            resS = 'S','s'
            resN = 'N','n'
            perg = input('Deseja cadastrar mais algum cliente: ')
            if perg == resN:
                pperg = input('Se deseja continuar com menu digite S, se deseja sair digite 7: ')
            elif pperg == resS:
                ''' 1 - Cadastro de Cliente
                    2 - Ver Clientes Cadastrados
                    3 - Cadastro de Produtos
                    4 - Ver Produtos Cadastrados
                    5 - Vendas
                    6 - Relatórios de Vendas
                    7 - Sair '''
        if n1 == '2':
            print('Clientes Cadastrados: ')
            for c in cadastro:
                print(cadastro)
        elif n1 == '3':
            print('Cadastro de Clientes: ')
        elif n1 == '4':
            print('Produtos Cadastrados: ')
        elif n1 == '5':
            print('Vendas')
        elif n1 == '6':
            print('Relatorios de Vendas: ')
        elif n1 == '7':
            print('Saindo do menu.')
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
    if n1 == '2':
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
elif n1 == '2':
    print('Clientes Cadastrados: ')
    for c in cadastro:
       print(f'{c+1} - {cadastro}')
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
        if n1 == '1':
            cadastro = input('Digite o nome do cliente: ')
            codigo = []
            codigo.append(cadastro)
            resS = 'S','s'
            resN = 'N','n'
            perg = input('Deseja cadastrar mais algum cliente: [S/N] ')
    while perg == resS:
        cadastro = input('Digite o nome do cliente: ')
        codigo.append(cadastro)
        resS = 'S','s'
        resN = 'N','n'
        perg = input('Deseja cadastrar mais algum cliente: ')
        if perg == resN:
            pperg = input('Se deseja continuar com menu digite S, se deseja sair digite 7: ')
        elif pperg == resS:
            ''' 1 - Cadastro de Cliente
                2 - Ver Clientes Cadastrados
                3 - Cadastro de Produtos
                4 - Ver Produtos Cadastrados
                5 - Vendas
                6 - Relatórios de Vendas
                7 - Sair '''
    if n1 == '2':
        print('Clientes Cadastrados: ')
        for c in cadastro:
            print(cadastro)
    elif n1 == '3':
        print('Cadastro de Clientes: ')
    elif n1 == '4':
        print('Produtos Cadastrados: ')
    elif n1 == '5':
        print('Vendas')
    elif n1 == '6':
        print('Relatorios de Vendas: ')
    elif n1 == '7':
        print('Saindo do menu.')
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
if n1 == '2':
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
# , CPF, Nome completo, 
# data de nascimento, Estado, Cidade, cep, bairro, rua, numero da casa, complemento.

# Quando chegar em casa vou aprimorar. com funções.