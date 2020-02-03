import MySQLdb
from PythonCourse.ProgramaHBSIS.Model.model_endereco import Endereco_cliente
from PythonCourse.ProgramaHBSIS.Model.model_cliente import Cliente

conexao = MySQLdb.connect(host= '127.0.0.1', database= 'db_ituroro', user= 'root', passwd= '')
cursor = conexao.cursor()

class Dao_Pessoas:
    def salvar(self):
        perg = 'n'
        while perg == 'n':
            nome = input('Digite o nome que deseja ser cadastrado: ')
            cpf = input('Digite o CPF: ')
            datanasc = input('Digite a data de nascimento: ')
            perg = input(f'Os dados cadastrados foram\nNome: {nome}\nCPF: {cpf}\nData de nascimento: {datanasc}\n\t Estão corretos? [S/N]: ')
        if perg == 's':
            cursor.execute(f"INSERT INTO clientes (nome , cpf, data_nasci)VALUES ('{nome}','{cpf}','{datanasc}')")
            conexao.commit()
    def listar_todos(self):
        cursor.execute("SELECT codigo_do_cliente, nome, cpf, data_nasci FROM clientes")
        resultado = cursor.fetchall()
        return resultado
    def leitura(self):
        self.listar_todos()
        contador = 0
        for pessoas in self.listar_todos():
            print(f'Grupo {contador}:\n')
            print(f'\n{pessoas}')
            contador += 1
    def atualizar_cadastro(self):
        self.leitura()
        id_escolhido = int(input('Digite o ID de quem você deseja alterar: '))
        print('''
        1 - Nome:
        2 - CPF:
        3 - Data Nascimento:
        ''')
        dado_escolhido = input('Digite o que você deseja alterar [1/2/3]:  ')
        if dado_escolhido == 1:
            perg = 'N','n','não','Não'
            while perg == 'N' or 'n' or 'não' or 'Não':
                novo_nome = input('Digite o novo nome: ')
                perg = input(f'Os dados cadastrados foram Nome: {novo_nome} \nEstão corretos? [Y/N]: ')
                cursor.execute(f"UPDATE clientes SET nome={novo_nome} WHERE codigo_do_cliente={id_escolhido}")
                conexao.commit()
        if dado_escolhido == 2:
            perg = 'N','n','não','Não'
            while perg == 'N' or 'n' or 'não' or 'Não':
                novo_cpf = input('Digite o novo cpf: ')
                perg = input(f'Os dados cadastrados foram CPF: {novo_cpf} \nEstão corretos? [Y/N]: ')
                cursor.execute(f"UPDATE clientes SET cpf={novo_cpf} WHERE codigo_do_cliente={id_escolhido}")
                conexao.commit()
        if dado_escolhido == 3:
            perg = 'N','n','não','Não'
            while perg == 'N' or 'n' or 'não' or 'Não':
                nova_datanasci = input('Digite a nova data de nascimento: ')
                perg = input(f'Os dados cadastrados foram Data de nascimento: {nova_datanasci} \nEstão corretos? [Y/N]: ')
                cursor.execute(f"UPDATE clientes SET data_nasci={nova_datanasci} WHERE codigo_do_cliente={id_escolhido}")
                conexao.commit()
    def deletar(self):
        self.leitura()
        id_escolhido = int(input('Digite o ID do cadastro do qual deseja deletar: '))
        cursor.execute(f"DELETE FROM clientes WHERE ID = {id_escolhido}")
        conexao.commit()

show = Dao_Pessoas()
show.salvar()
