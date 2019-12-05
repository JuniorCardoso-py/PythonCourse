# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


# 2 - usando o for, imprima todos nomes um abaixo do outro
#
# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)
print(f'Nome: {cadastroHBSIS[1][0]} telefone: {cadastroHBSIS[3][0]}')
print(f'Idade: {cadastroHBSIS[1][4]} Idade: {cadastroHBSIS[7][4]}')
print(f'Email: {cadastroHBSIS[1][3]} Email: {cadastroHBSIS[5][3]}')

n1 = []
for e in cadastroHBSIS:
    n1.append(e)

cont = 0
for opcao in range(7):
    dicionario = {'nome':n1[1][cont],'email':n1[5][cont],'idade':n1[7][cont], 'telefone':n1[3][cont] }
    print(f"Nome: {dicionario['nome']} - Email: {dicionario['email']} - Idade: {dicionario['idade']} - Telefone: {dicionario['telefone']}")
    lista = dicionario
    cont = cont +1


        







# print(cadastroHBSIS[0])
# print(cadastroHBSIS[1])
# print(cadastroHBSIS[2])
# print(cadastroHBSIS[3])
# print(cadastroHBSIS[4])
# print(cadastroHBSIS[5])
# print(cadastroHBSIS[6])
# print(cadastroHBSIS[7])
