import MySQLdb
from time import sleep
from PythonCourse.Sorteio.ModelSorteio.model_lista_alunos import Alunos

conexao = MySQLdb.connect(host='127.0.0.1', database='alunossala', user='root', passwd='')
cursor = conexao.cursor()
class Crud_sorteio:
    def listar(self):
        cursor.execute("SELECT * FROM nomes_alunos ")
        resultado = cursor.fetchall()
        return resultado

    def salvar(self):
        print('''   Menu de Inserção de alunos  ''')
        perg = 'S'
        while perg == 'S':
            n1 = input('\n Digite o nome a ser cadastrado: ')
            confirm = input(f'\nO nome cadastrado foi {n1} está correto? [S/N]: ').upper()
            if confirm == 'S':
                cursor.execute(f"INSERT INTO nomes_alunos(Nomes)Values('{n1}')")
                conexao.commit()
                print('\t\tCadastrado com sucesso!')
                perg = input(('\nDeseja cadastrar mais alguem? [S/N]: ')).upper()
            else:
                print('\nDigite novamente\n')
        print('\t\t\t\t\nSaindo do Programa')

    def atualizar(self):
        print('''       Menu de Atualização da Tabela    ''')
        perg = 'S'
        while perg == 'S':
            for pessoa in self.listar():
                print(f'ID:{pessoa[0]} Nome: {pessoa[1]}')
            id = int(input('\nAqui estão as pessoas cadastradas, digite o ID do cadastro que deseja atualizar: '))
            nome = input('Digite o nome a ser alterado: ')
            confirm = input(f'\nO nome a ser alterado foi {nome} está correto? [S/N]: ').upper()
            if confirm == 'S':
                cursor.execute(f"UPDATE nomes_alunos SET Nomes ='{nome}' where ID ={id} ")
                conexao.commit()
                print('\t\tAlterado com sucesso!')
                perg = input('Deseja Alterar mais algum cadastro? [S/N]').upper()
            else:
                print('\t\tDigite Novamete!!\n')
                sleep(2)
        print('\t\t\t\t\nSaindo do Programa')

    def deletar(self):
        print('''       Bem vindo ao    
                    Menu de remoção de dados da tabela    ''')
        sleep(3)
        perg = 'S'
        while perg == 'S':
            for pessoa in self.listar():
                print(f'ID:{pessoa[0]} Nome: {pessoa[1]}')
            id = int(input('\nAqui estão as pessoas cadastradas, digite o ID do cadastro que deseja deletar: '))
            nome = input('Digite o nome a ser deletado: ')
            confirm = input(f'\nO nome selecionado foi {nome} está correto? [S/N]: ').upper()
            if confirm == 'S':
                cursor.execute(f"DELETE FROM nomes_alunos where ID={id}")
                conexao.commit()
                print('\t\t\tCadastro deletado com sucesso\n')
                perg = input('Deseja deletar mais algum cadastro? [S/N]').upper()
            else:
                print('\t\tDigite Novamete!!\n')
                sleep(2)
        print('\t\t\t\t\nSaindo do Programa')

    def buscar_por_nome(self):
        nome = input('Digite o nome ou uma palavra chave que deseja buscar na lista: ')
        cursor.execute(f"SELECT * FROM nomes_alunos WHERE Nomes LIKE '%{nome}%'")
        lista_de_resultados = []
        resultado = cursor.fetchall()
        print(resultado)
        for pessoas in resultado:
            lista_de_resultados.append(pessoas)
        lista_nova = []
        for elementos in lista_de_resultados:
            for dados_lista in elementos:
                lista_nova.append(dados_lista)
        print(lista_nova)
        lista_dicionario = []
        print((len(lista_nova)))
        for elemento in lista_nova[:2:]:
            dicionario = {'numero_id': 0, 'nome': ''}
            dicionario['numero_id'] = elemento
            lista_dicionario.append(dicionario)
            print(dicionario)
        print(lista_dicionario)
show = Crud_sorteio()
show.buscar_por_nome()








