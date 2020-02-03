# Aula 28 - 17-12-2019
# Revisão de listas, arquivo

# 1) Faça um programa de sorteio de alunos.
# Especificações:
# - Deve sortear um aluno por vez.
# - O programa deve garantir que todos os alunos sejam sorteados antes de reiniciar
# o sorteio.
# - O programa deve garantir que mesmo que ele seja fechado, o sorteio dos alunos só
# seja reiniciado quando todos os alunos forem sorteados.
# - Faça um menu para o program e de destaque para o aluno sorteado.


# Dica:
# Ovo de pascua
# O "import os" pode habiliar alguns comandos como o os.system() que pode passar comando
# do DOS, shell script do python para o terminal.
#
# Como vocês ainda não sabem o que é o import e como ele funciona, então o pode-se trocar por:
#
# from os import system
# system('dir')
#
# Agora imagine se usar o system('cls') para windows ou system('clear') para linux
# o cls/clear apaga o que foi impresso anteriormente na tela do terminal.
#
#
# :-)
# Poste no grupo do whatsapp #ACHEI! se vc ler esta mensagem!
# (ninguem achou este ovo de pascua!)
import random
from time import sleep
import MySQLdb

conexao = MySQLdb.connect(host ='localhost', database ='sorteio', user='root', passwd ='')
cursor = conexao.cursor()
def Upadte_tabela():
    quantidade_alunos = int(input('Digite a Quantidade de Alunos a serem cadastrados para o sorteio: '))
    lista = []
    for aluno in range(quantidade_alunos):
        print(f'Cadastro de Aluno para Sorteio! {aluno + 1}')
        aluno1 = input('Digite o nome do aluno: ')
        lista.append(aluno1)
        comandoSQL = cursor.execute
        comandoSQL(f"INSERT INTO lista_alunos (Nomes) VALUES('{aluno1}')")
        conexao.commit()
    print(f'\nCadastrado um total de {len(lista)} alunos\n')
    sorteado = random.choice(lista)
    print(f'O Aluno sorteado foi: {sorteado}\n\t\t Congratulations!!')
    for sorteado in lista:
        lista.remove(sorteado)
        print(mostra_lista())
        perg = input('Deseja continuar? [S/N]')
    if perg == 'S' or 's':
        print('Sorteando novamente!')
        sleep(2)
        sorteado = random.choice(lista)
        print(f'O Aluno sorteado foi: {sorteado}\n\t\t Congratulations!!')
        for sorteado in lista:
            lista.remove(sorteado)
            print(mostra_lista())
            perg = input('\nDeseja continuar? [S/N]')
    if perg == 'N' or 'n':
        print('\nAté a proxima!')
        return Menu()
def deletar():
    comandoSQL = cursor.execute
    comandoSQL(f"SELECT * FROM lista_alunos")
    lista = cursor.fetchall()
    for pessoa in lista:
        print(pessoa)
    quantidade = input('Deseja excluir varios cadastros?: [S/N]')
    if quantidade == 'S' or 's':
        nome = str(input('Digite o Nome a ser excluido da lista: '))
        comandoSQL(f"DELETE FROM lista_alunos WHERE Nomes={nome}")
        conexao.commit()
        perg1 = input('Deseja deletar mais alguem?: [S/N]: ')
        if perg1 == 'S' or 's':
            nome = str(input('Digite o Nome a ser excluido da lista: '))
            comandoSQL(f"DELETE FROM lista_alunos WHERE Nomes={nome}")
            conexao.commit()
            while perg1 != 'S' or 's':
                return perg1
    elif quantidade == 'N' or 'n':
        nome = str(input('Digite o Nome a ser excluido da lista: '))
        comandoSQL(f"DELETE FROM lista_alunos WHERE Nomes={nome}")
        conexao.commit()
        print(f'Restaram o seguintes dados na lista {lista}')
        perg = input('Deseja deletar mais alguem?: [S/N]: ')
        if perg == 'S' or 's':
            return deletar()
        else:
            return Menu()
def alterar():
    comandoSQL = cursor.execute
    comandoSQL("SELECT * FROM lista_alunos")
    lista= cursor.fetchall()
    for p in lista:
        print(p)
    id = input('Digite o numero da posição onde se encontra o Aluno a ser atualizado: ')
    novo_nome = input('Agora digite o nome que deseja atualizar: ')
    comandoSQL(f"UPDATE lista_alunos SET Nomes ='{novo_nome}' WHERE IDALUNO = {id}")
    conexao.commit()
    return Menu()
def mostra_lista():
    comandoSQL = cursor.execute
    comandoSQL("SELECT * FROM lista_alunos")
    lista= cursor.fetchall()
    for p in lista:
        print(p)
    return Menu()
def Menu():
    print('\n\tBem Vindo ao Menu de Sorteio!!\n')
    n1 = input('Se Deseja adicionar alunos na tabela digite [1] ou pressione ENTER para a proxima opção: ')
    if n1 == '1':
        Upadte_tabela()
    else:
        pass
    n2 = input('\nSe Deseja Visualizar a lista com os nomes cadastrados digite [2] ou pressione ENTER para a proxima opção:  ')
    if n2 == '2':
        mostra_lista()
    else:
        pass
    n3 = input('\nSe Deseja Alterar algum nome da tabela de sorteio digite [3] ou pressione ENTER para a proxima opção:  ')
    if n3 == '3':
        alterar()
    else:
        pass
    n4 = input('\nSe deseja Deletar algum dado da tabela de sorteio digite [4] ou pressione ENTER para a proxima opção: ')
    if n4 == '4':
        deletar()
    else:
        pass
    n0 = input('\nSe Deseja Sair do menu digite [0]: ')
    if n0 == '0':
        print('\n\tObrigado Volte Sempre!')
Menu()