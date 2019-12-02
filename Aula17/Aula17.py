# 1 - Faça um menu interartivo que tenha: Cadastro da banda, cadastro do album
# Cadastro da musica e sair
# O menu deve ser executado até que se escolha a opçao sair
# cada opção deve ser mostrada
# quando selecionado a opçao sair deverá apareceer na tela as informações das
# bandas cadastradas.
# albuns e musica.

print('#'*50)
print('\t'*2,'Cadastro de Bandas')
print('#'*50)

print('1 - Cadastro da Banda: \n2 - Cadastro do album: \n3 - Cadastro da musica: \n4 - Cadastrar tudo: \n5 - Sair')
n1 = input('Digite um numero para entrar no menu desejado: ')

opcao = ['1','2','3','4','5']

if n1 == '1':
    nome_banda = input('Cadastre o nome da banda: ')
    print(f'O nome da Banda cadastrada é {nome_banda}. Parabéns!!')
elif n1 == '2':
    nome_album = input('Cadastre o nome do album: ')
    print(f'O nome do album cadastrado é {nome_album}. Parabéns!!')
elif n1 == '3': 
    nome_musica = input('Cadastre o nome da musica: ')
    print(f'O nome da musica cadastrada é {nome_musica}. Parabéns!!')
elif n1 == '4':
    nome_banda = input('Cadastre o nome da banda: ')
    nome_album = input('Cadastre o nome do album: ')
    nome_musica = input('Cadastre o nome da musica: ')
    print(f'\n\tBanda Cadastrada com sucesso: ')
    print(f'\n{nome_banda}\n{nome_album}\n{nome_musica}')
elif n1 == '5':
    print('Saindo do menu.')
while n1 not in opcao:
    print('Opção invalida! Digite somente os numeros sugeridos')
    n1 = input('Digite um numero para entrar no menu desejado: ')
    if n1 == '1':
        nome_banda = input('Cadastre o nome da banda: ')
        print(f'O nome da Banda cadastrada é {nome_banda}. Parabéns!!')
    elif n1 == '2':
        nome_album = input('Cadastre o nome do album: ')
        print(f'O nome do album cadastrado é {nome_album}. Parabéns!!')
    elif n1 == '3': 
        nome_musica = input('Cadastre o nome da musica: ')
        print(f'O nome da musica cadastrada é {nome_musica}. Parabéns!!')
    elif n1 == '4':
        nome_banda = input('Cadastre o nome da banda: ')
        nome_album = input('Cadastre o nome do album: ')
        nome_musica = input('Cadastre o nome da musica: ')
        print(f'\n\tBanda Cadastrada com sucesso: ')
        print(f'\n{nome_banda}\n{nome_album}\n{nome_musica}')
    elif n1 == '5':
        print('Saindo do menu.')