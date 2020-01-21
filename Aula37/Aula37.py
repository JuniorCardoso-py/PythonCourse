# Criar uma pagina para cadastro de squads (times de desenvolvimento)
# 1 - Criar Tabela Squad
# 2 - Criar dao Squad
# 3 - Criar Model Squad
# 4 - Criar controller Squad
# 5 - Criar View tipo conselo para realizar as 4 operações de CRUD de Squads
# 6 - Criar View tipo web para realizar as 4 operaçoes de CRUD
# Squad: Nome, Descrição, NumeroPessoas,LinguagemBackEnd,
import MySQLdb
conexao=MySQLdb.connect(host='127.0.0.1', database='squads', user='root', passwd='')
cursor = conexao.cursor()

def salvar():
    cursor.execute('SELECT * FROM SQUAD')
    resultado = cursor.fetchall()
    print(resultado)
    perg = input('Deseja adicionar algum time? [Y/N]: ')
    if perg == 'Y' or 'y':
        nome = input('Digite o nome: ')
        descri = input('Digite a descrição: ')
        numpessoas = int(input('Digite o numero de pessoas no time: '))
        linguagem = input('Digite a linguagem de programção do time: ')
        frame = input('Digite  o framework utilizado:  ')
        cursor.execute(f"INSERT INTO SQUAD (Nome, Descrição, NumeroPessoas, LinguagemBackEnd, FrameworkFrontEnd) VALUES ('{nome}','{descri}',{numpessoas},'{linguagem}','{frame}')")
        conexao.commit()
    elif perg != 'Y' or 'y':
        print('Fim do programa')


def alterar():
    print('\t\tBem Vindo ao Sistema de alteração!!!')
    print('O que Deseja alterar no cadastro?: ')
    print('\nNome [1]')
    print('\nDescrição [2]')
    print('\nNumeroPessoas [3] ')
    print('\nLinguagemBackEnd [4]')
    print('\nFrameworkFrontEnd [5]')
    print('\nTodas [6]')
    resp = input('\n\tQual opção deseja alterar?: ')
    if resp == '1':
        cursor.execute('SELECT * FROM SQUAD')
        id = cursor.fetchall()
        print(id)
        id = int(input('Qual o Id do time que deseja alterar?: '))
        nome = input('Digite o novo nome do time: ')
        cursor.execute(f"UPDATE SQUAD SET Nome = '{nome}' WHERE ID={id} ")
        conexao.commit()
    elif resp == '2':
        cursor.execute('SELECT * FROM SQUAD')
        id = cursor.fetchall()
        print(id)
        id = int(input('Qual o Id do time que deseja alterar?: '))
        descri = input('Digite a nova descrição  do time: ')
        cursor.execute(f"UPDATE SQUAD SET escrição = '{descri}' WHERE ID={id} ")
        conexao.commit()
    elif resp == '3':
        cursor.execute('SELECT * FROM SQUAD')
        id = cursor.fetchall()
        print(id)
        id = int(input('Qual o Id do time que deseja alterar?: '))
        numero_pessoas = int(input('Digite a quantidade de pessoas no time: '))
        cursor.execute(f"UPDATE SQUAD SET NumeroPessoas = {numero_pessoas} WHERE ID={id} ")
        conexao.commit()
    elif resp == '4':
        cursor.execute('SELECT * FROM SQUAD')
        id = cursor.fetchall()
        print(id)
        id = int(input('Qual o Id do time que deseja alterar?: '))
        linguagem = input('Digite a linguagem  de programação do time: ')
        cursor.execute(f"UPDATE SQUAD SET LinguagemBackEnd = '{linguagem}' WHERE ID={id} ")
        conexao.commit()
    elif resp == '5':
        cursor.execute('SELECT * FROM SQUAD')
        id = cursor.fetchall()
        print(id)
        id = int(input('Qual o Id do time que deseja alterar?: '))
        framework = input('Digite o framework utilizado time: ')
        cursor.execute(f"UPDATE SQUAD SET FrameworkFrontEnd = '{framework}' WHERE ID={id} ")
        conexao.commit()
    elif resp == '6':
        cursor.execute('SELECT * FROM SQUAD')
        id = cursor.fetchall()
        print(id)
        id = int(input('Qual o Id do time que deseja alterar?: '))
        nome = input('Digite o novo nome do time: ')
        descri = input('Digite a nova descrição  do time: ')
        numero_pessoas = int(input('Digite a quantidade de pessoas no time: '))
        linguagem = input('Digite a linguagem  de programação do time: ')
        framework = input('Digite o framework utilizado time: ')
        cursor.execute(f"UPDATE SQUAD SET Nome = '{nome}', Descrição = '{descri}', NumeroPessoas = {numero_pessoas}, LinguagemBackEnd = '{linguagem}', FrameworkFrontEnd = '{framework}' WHERE ID={id} ")
        conexao.commit()
alterar()


