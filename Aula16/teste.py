def criar_faixa(musica, banda, album):
    faixa = {'musica':musica, 'artista':banda, 'album':album}
    return faixa

# funções interligadas

def salvar_faixa(faixa):
    arquivo = open('Aula16/faixas.txt','a')
    arquivo.write(f"{faixa['musica']};{faixa['artista']};{faixa['album']}\n")
    arquivo.close()
    return faixa

def ler_faixa():
    arquivo = open('Aula16/faixas.txt','r')
    lista_faixas = []
    for linha in arquivo: # Aqui ele vai ler todos o elementos dentro da variavel arquivo
        linha = linha.strip() # limpo linha
        dados_faixa = linha.split(';') # condição de separação das strings
        faixa = criar_faixa(dados_faixa[0],dados_faixa[1],dados_faixa[2])
        lista_faixas.append(faixa) # adicionar todos os dados da variavel faixa para uma lista
    arquivo.close() # sempre fechar usando esse metodo.
    return lista_faixas