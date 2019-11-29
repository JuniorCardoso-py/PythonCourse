# Aula 16 - 29/11/2019 
# ?????????
#Crie um metodo
#cadastro de playlist
#lendo musica, artista e album
from teste import criar_faixa

musica = input('Digite o nome da musica: ')
banda = input('Digite o nome da banda: ')
album = input('Digite o nome do album da musica: ')
#dados_banda = [musica,banda,album]
#faixa = {'musica':musica, 'artista':banda, 'album':album}
faixa = criar_faixa(musica,banda,album)

open('faixas.txt','a')
