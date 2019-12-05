# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)
dados = []
for a in pess:
        dados.append(a)
cont = 0
lista = []
for cadastros in range(len(pess[0])):
        dicionario = {'nome':dados[0][cont],'telefone':dados[1][cont],'email':dados[2][cont],'idade':int(dados[3][cont])}
        lista.append(dicionario)
        cont = cont +1
n1 = []

# lista = n1
# [{'nome': 'Alex', 'telefone': '4799991', 'email': 'a@a.com', 'idade': 18}, 
# {'nome': 'Paulo', 'telefone': '4799992', 'email': 'b@b.com', 'idade': 25}, 
# {'nome': 'Pedro', 'telefone': '4799993', 'email': 'c@c.com', 'idade': 40}, 
# {'nome': 'Mateus', 'telefone': '4799994', 'email': 'd@d.com', 'idade': 16}, 
# {'nome': 'Carlos', 'telefone': '4799995', 'email': 'e@e.com', 'idade': 15},
# {'nome': 'João', 'telefone': '4799996', 'email': 'f@f.com', 'idade': 19}, 
# {'nome': 'Joaquim', 'telefone': '4799997', 'email': 'g@g.com', 'idade': 17}]


for dados in lista: # Aqui não estou usando a variavel dados de cima
        # dados = {'nome': 'Alex', 'telefone': '4799991', 'email': 'a@a.com', 'idade': 18}
        print(f"{dados['nome']} - {dados['telefone']} - {dados['email']} - {dados['idade']}")
        n1.append(dados)

if len(n1) < 18:  # if 7 < 18 
        
        # dados = {'nome': 'Joaquim', 'telefone': '4799997', 'email': 'g@g.com', 'idade': 17}
        menor = []
        # menor = []
        menor.append(dados['nome'])
        print(f'\nLista dos menores de idade que não poderam participar:{menor}\n')

# menor = ['Joaquim']