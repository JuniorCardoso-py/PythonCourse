# Aula 16 - 29-11-2019
# Funções

#--- Importação das funções criadas para manipulação das faixas de uma playlist
#--- Importação é feita indicando primeiramente o arquivo para a palavra-chave 'from'
#--- Depois é feita a importação de cada função após a paravra-chave 'import'
#--- É possível fazer a importação de todas as funções de um arquivo utilizando '*' após a palavra-chave 'from'
from faixa import criar_faixa, salvar_faixa, ler_faixas


#cadastro de playlist
#lendo dados do terminal, musica, artista e album
musica = input('Digite uma musica: ')
album = input('Digite o nome do album: ')
artista = input('Digite o nome do artista: ')

#---  Chama a função criar_faixa() e passa os dados lidos do terminal 
#---  A função ciar_faixa() retorna um dicionário criado com os dados enviados a ela
faixa1 = criar_faixa(musica, album, artista)

#--- Chama a função criar_faixa() e passa como parâmetro o dicionário retornado pela função criar_faixa()
#--- A função criar_faixa() salva o dicionário e nao retorna nenhum dado
salvar_faixa(faixa1)

#--- Chama a função ler_faixas(), a função não necessita de nenhum parâmetro
#--- A função lê todas as faixas salvas, cria um dicionário para cada faixa e adiciona em uma lista
#--- Função retorna a lista de dicionários
lista = ler_faixas()

#--- For para leitura da lista de dicionários retornada pela função ler_faixas()
#--- É feita a impressão no terminal dos dados de cada dicionário contido na lista 
#--- A impressão é feita através das chaves do dicionário e utilizando f-strings na função print()
for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}')