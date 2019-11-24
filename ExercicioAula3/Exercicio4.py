#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variávies para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuario e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuario e senha estejam incorretos informe com mensagem de falha de login

print('@'*20,'Autenticação de Usuario','@'*20)

login = input('Digite seu Login:  ')
senha = int(input('Digite sua senha: '))

logpad = 'JuniooRBR'
senpad = int(123456)

if logpad == login and senpad == senha:
    print('Dados corretos acesso liberado!!')
while logpad != login:
    print('Login com dados errados digite novamente:')
    login = input('Digite seu Login:  ')
    if login == logpad and senpad == senha:
        print('Dados corretos acesso liberado!!')
while senpad != senha:
    print('Senha com dados errados digite novamente:')
    senha = int(input('Digite sua senha: '))
    if senpad == senha and logpad == login:
        print('Dados corretos acesso liberado!!')

