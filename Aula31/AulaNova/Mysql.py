import MySQLdb

def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

def buscar_por_sobrenome(c, sobrenome):
    c.execute(f'SELECT * FROM pessoa WHERE SOBRENOME = {sobrenome}')
    pessoa = c.fetchone()
    print(pessoa)

def buscar_por_inicio_palavra(c, sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE SOBRENOME like '{sobrenome}%'")
    pessoa = c.fetchall()
    print(pessoa)

def salvar(cn,cr,nome,sobrenome,idade,endereco_id='NULL'):
    cr.execute(F"INSERT INTO pessoa (NOME,SOBRENOME,IDADE,ENDERECO_ID)VALUES('{nome}','{sobrenome}',{idade},{endereco_id})")
    cn.commit()

def alterar(cn,cr,id,nome,sobrenome,idade,endereco_id):
    cr.execute(f"UPDATE pessoa SET NOME='{nome}' ,SOBRENOME='{sobrenome}' ,IDADE= {idade} ,ENDERECO_ID={endereco_id} WHERE ID ={id}")
    cn.commit()

def deletar(cn,cr,id):
    cr.execute(f'DELETE FROM pessoa WHERE ID={id}')
    cn.commit()
def retorno(a):
    return a

conexao = MySQLdb.connect(host='127.0.0.1', database='junior_aula_bancodados',user='root',passwd='')
cursor = conexao.cursor()

def add_via_input(cn,cr):
    print('Adicionando novos dados a Tabela!!\n')
    nome = input('Digite o nome para cadastro: ')
    sobrenome = input('Digite o sobrenome para cadastro: ')
    idade = int(input('Digite o idade para cadastro: '))
    endereco_id = int(input('Digite o numero do endereço cadastrado: '))
    cr.execute(f"INSERT INTO pessoa (NOME,SOBRENOME,IDADE,ENDERECO_ID)VALUES('{nome}','{sobrenome}',{idade},{endereco_id})")
    cn.commit()
    perg = input(str('Deseja Cadastrar mais alguem? [S/N]: '))
    if perg == 'S':
        return add_via_input(cn,cr)
    elif perg == 'N':
        print('Obrigado Volte sempre')
    else:
        print('Digite somente a letra S para sim e N para não!')
        return perg
    listar_todos(cursor)

add_via_input(conexao, cursor)
#alterar(conexao, cursor,4,'Voltolini','KingOfbasquete',16,4)
#salvar(conexao,cursor,'Oi','Tchau',50,4)
#listar_todos(cursor)
#buscar_por_id(cursor, 3)
#deletar(conexao, cursor,7)