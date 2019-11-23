#--- Exercicio 3  - Variávies e impressão com interpolacão de string
#--- Imprima dois paragráfos do ultimo livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- Livro: Título, Edição, Autor, Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

print('Dois paragrafos do Livro: Principios de Bancos de Dados \n')

print('''\tUm banco de dados também pode ser chamado de base de dados. Os dados
são armazenados de uma maneira que tem como objetivo facilitar a inclusão,
remoção, consulta e alteração. Eles representam aspectos ou fatos do mundo
real, que muitas vezes é denominado de minimundo ou universo de discurso. Só
devemos armazenar no banco de dados o que faz parte do seu minimundo.
\n\tPara exemplificar melhor, pense em um sistema de vendas de ingressos
online para cinemas. Nesse minimundo existem características que são importantes
e necessárias para a venda de ingressos, como por exemplo, o nome do filme,
horário em que ele será reproduzido, o local, se é dublado ou legendado etc. Essas
características precisam estar armazenadas para possíveis consultas e alterações.
Já características como a cor das paredes ou o tipo de piso da sala do cinema não
são fatos necessários para posterior consulta em um sistema e não precisam ser
armazenados no banco de dados.''')

dadoss = ['Prof. Décio Lehmkuhl' , 'Prof. Djayson Roberto Eger' ,'Principio de Banco de Dados', 'Centro Universitário Leonardo da Vinci – UNIASSELVI' , 'Uniasselvi, 2013.']

print(f'\n Autor: {dadoss[0] , dadoss[1]} \n Edição: {dadoss[3]} \n Titulo: {dadoss[2]} \n Data de publicação: {dadoss[4]}')