#--- Exercicio 2  - Variávies e impressão com interpolacão de string
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format() para concatenar os números da opções,
#  que devem ser números inteiros
#--- Alem das opções o menu deve conter um cabeçalho e um rodapé
#--- O cabeçalho e o rodapé devem ser impressos utilizando a multiplicação de caracters
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação 

print('#'*20,'Isso é um cabeçalho','#'*20,'\n'*3)

print('Cadastramento de funcionarios HBSIS')

n1 = input('\nQual o nome do funcionario?: ')
n2 = input('\nQual o sobrenome?: ')
n3 = int(input('\nDigite o CPF: '))
n4 = int(input('\nDigite o RG: '))
n5 = int(input('\nQual o seu salario?:  '))

print(f'\nO nome completo do funcinario é: {n1} {n2}\n O seu CPF é: {n3} \n O seu RG é : {n4} \n E o seu salario é: R${n5:.2f}')

print('\t'*6,'\n'*3,'#'*20,'Isso é um rodapé','#'*20)