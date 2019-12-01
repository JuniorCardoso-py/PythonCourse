#--- Arquivo contendo as funções para a manipulação de faixas de uma playlist
#--- Toda a manipulação de dados relacionadas as faixas estará contida em funções neste arquivo

#--- Função que cria uma estrutura para agrupar os dados de uma faixa musical
#--- A estrutura de dados utilizada para agrupar os dados é um dicionário
#--- O dicionário é uma estrutura composta por chave-valor, esta estrutura foi abordada na Aula 7
#--- A função recebe os dados para a crição de uma faixa musical através de parâmetros
#--- É feita a criação de um dicionário onde os valores são compostos pelos parâmetros recebidos na função
#--- Após a criação do dicionário é feito o retorno através da palavra-chave 'return' e a variável que contem o dicionário
def criar_faixa(musica, album, artista):
    faixa = {'musica': musica, 'album':album, 'artista':artista }
    return faixa

#--- Função para salvar os dados de uma faixa
#--- A função salva os dados em um arquivo texto que foi criado na pasta desta aula
#--- A função realiza a abertura do arquivo texto e utiliza o parametro 'a' na função open, 
#--- O parâmetro 'a' indica que será adicionado dados ao arquivo aberto
#--- O arquivo aberto é atribuido a variável 'arquivo' e é utilizada a função write para escrever os dados no arquivo texto
#--- Na função write é utilizado f-strings para a formatação da string a ser salva no arquivo e é concatenado cada dado do dicionario
#--- Os dados do dicionários são extraidos da variável que foi recebida como parâmetro nesta função
#--- Cada dado é lido através das chaves do dicionário que foi criado pela função criar_faixa(), contida neste arquivo
#--- A formatação da string é feita separando cada dado do dicionário com um ponto e virgula ';' para facilitar uma leitura deste arquivo texto
#--- Após inserir os dados no arquivo texto é chamada a função close() para que o arquivo seja fechado.
def salvar_faixa(faixa):
    arquivo = open('16-Aula16/faixas.txt','a')
    arquivo.write(f'{faixa["musica"]};{faixa["album"]};{faixa["artista"]}\n')
    arquivo.close()

#--- Função que lê as faixas musicais salvas
#--- A função não recebe nenhum dado por parâmetro, já que ela mesma ja possuí todos os dados necessário para sua execução
#--- É feita a abertura do arquivo texto 'faixas.txt' contido na pasta desta aula
#--- Esta arquivo texto contém todas as faixas salvas pela função salvar_faixa(), função esta que está neste mesmo arquivo
#--- O arquivo é aberto pela função 'open()' e atribuido à variável 'arquivo'
#--- É utilizado a estrutura de repetição for para a leitura de todas as linhas contidas neste arquivo
#--- Na primeira linha do for é utilizado a função 'strip()' que remove todos os espaços em branco antes de depois da linha e tambem o caracter \n
#--- Na segunda linha do for é utilizada a função 'split()' e passado como parâmetro o caracter ponto e virgula ';'
#--- A função split faz a separação da string que repesenta a linha do arquivo
#--- Ela separa a string baseando-se no caracter enviado por parâmetro, neste caso o ponto e virgula ';'
#--- Ela separa cada parte da string antes e depois deste caracter e envia cada parte da string para uma posicao de uma lista
#--- Portando o retorno da função 'split()' é uma lista que contém em cada posição uma parte da string que foi separada baseada no caracter passado como parâmetro
#--- O caracter passado para a função é o mesmo utilizado para separar os dados na hora de salvar o dicionario da faixa musical
#--- Neste caso cada item da lista gerada pela função 'split()' é um dado do dicionário faixa musical
#--- Na terceira linha do for é feita a chamada da função 'criar_faixa()' e passado cada posição da lista como parâmetro
#--- O retorno da função 'criar_faixa()' é atribuido a variável faixa e adicionado a lista de faixas através da função 'append()'
#--- Após a execução do 'for' é feito o fechamento do arquivo através da função 'close()'
#--- A lista de faixas é retornada na ultima linha da função através da instrução 'return' 
def ler_faixas():
    arquivo = open('16-Aula16/faixas.txt','r')
    lista_faixas = []
    for linha in arquivo:
        linha = linha.strip()
        dados_faixa = linha.split(';')
        faixa = criar_faixa(dados_faixa[0], dados_faixa[1], dados_faixa[2])
        lista_faixas.append(faixa)
    arquivo.close()
    return lista_faixas