#--- Exercicio 2  - Impressão de dados com a função Input
#--- Imprima o menu de uma aplicação de cadastro de pessoas
<<<<<<< HEAD
#--- O menu deve conter as opções de Cadastrar, Alterar, listar pessoas, alem da opção sai.

n1 = []

for a in range(1,3):
    n1.append(input('Qual o seu Nome?: '))
    n1.append(input('Qual sua idade?: '))
    n1.append(input('Qual cidade mora?: '))
print(n1)

n2 = input('Deseja alterar o dado de algum usuario?: ')
resS= Sim 
resN= Não
if n2 == resS:
    dado_alterado=(input('Qual o nome do usuario que gostaria de alterar o dado?: '))
    if dado_alterado == [0]:
        del n1[0]
        n1.append(dado_alterado)
=======
#--- O menu deve conter as opções de Cadastrar, Alterar, listar pessoas, alem da opção sair 

>>>>>>> fb2c8596a926602f0635d0542fe45ed375746fbe
