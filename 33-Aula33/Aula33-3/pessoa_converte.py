def converter_tabela_dicionario(lista_tuplas):
    #cria uma lista para armazenar os dicionarios
    lista_pessoas = []
    for p in lista_tuplas:
        #----- Criação do dicionario que representa uma pessoa
        dicionario_pessoa = {'Id': 0, 'Nome' : '', 'Sobrenome': '', 'Idade' : 0, 'Endereco_Id': 0}
        #--- pega cada posição da tupla e atribui a uma chave do dicionário
        dicionario_pessoa['Id'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_Id'] = p[4]
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas