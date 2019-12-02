# Aula 16 - 29/11/2019 
# ?????????
#Crie um metodo
#cadastro de playlist
#lendo musica, artista e album
from teste import criar_faixa, salvar_faixa, ler_faixa #Chamar duas funções separar por virgulas.

musica = input('Digite o nome da musica: ') # adicionando dado para colocar dentro de um metodo que vai receber a variavel para salvar dentro de um arquivo texo
banda = input('Digite o nome da banda: ') # adicionando dado para colocar dentro de um metodo que vai receber a variavel para salvar dentro de um arquivo texo
album = input('Digite o nome do album da musica: ') # adicionando dado para colocar dentro de um metodo que vai receber a variavel para salvar dentro de um arquivo texo
#dados_banda = [musica,banda,album] # Aqui fiza só para ver como fica
faixa = {'musica':musica, 'artista':banda, 'album':album} # Aqui criei um dicionario para depois poder chamar na função pela chave de cada variavel adicionada
faixa = criar_faixa(musica,banda,album) # Aqui criei uma variavel que vai receber o metodo de criar uma faixa que vai receber o dicionario criado acima
save = salvar_faixa(faixa) # aqui criei uma variavel que vai receber o metodo que vai receber o que o metodo que vai salvar dentro do arquivo texto, oque será escrito 
lista = ler_faixa() # pode salvar dentro de uma variavel ou dar um print # Aqui vai receber o metodo para leitura doq esta dentro do arquivo texto para leitura dentro do console

for faixa in lista:
    print(f"{faixa['musica']} - {faixa['artista']} - {faixa['album']}")
