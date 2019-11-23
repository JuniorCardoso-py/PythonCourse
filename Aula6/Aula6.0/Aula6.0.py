idade = int(input('Qual sua idade? '))

#---- If com else,
#---- Caso a condição validada pelo if seja verdadeira
#---- O else é executado

if idade < 18:
    print('Dimenor')
else:
    print('Dimaior')
#If com elif e else 
#
#---- Caso a condição do elif seja falsa
#else é executado
if idade < 18:
    print('Dimenor')
elif idade == 18:
    print('Silasco')
else:
    print('SilascoMaisAinda')

#If com variavel booleana
#Em caso de variavel booleana, não é necessario a validação (== True)
#Pois o If ja valida o se conteudo de variavel é True,  
ativo = True
if ativo:
    print('Logar')
else:
    print('Não pode')

ativo = False
if ativo:
    print('Logar')
else:
    print('Não pode logar')


