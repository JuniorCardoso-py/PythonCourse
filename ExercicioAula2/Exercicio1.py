#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um 
# em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas 
# após a vírgula 


n1 = input('Qual o nome do funcionario?: ')
n2 = input('Qual o sobrenome?: ')
n3 = input('Digite o CPF: ')
n4 = input('Digite o RG: ')
n5 = float(input('Qual o seu salario?:  '))

print(f'O nome completo do funcinario é: {n1} {n2}\n O seu CPF é: {n3} \n O seu RG é : {n4} \n E o seu salario é: R${n5:.2f}')
