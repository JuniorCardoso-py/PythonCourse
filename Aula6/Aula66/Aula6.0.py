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


#Variavel booleana simples com true ou false
validador = False
# Substituição do valor inicial
validador = True

# Criação de variavel booleana atraves de expressão
idade = 18
validador = ( idade == 18) # igual que
print(validador)
validador = ( idade != 18) # diferente de
print(validador)
validador = ( idade > 18) # maior que
print(validador)
validador = ( idade < 18) # menor que
print(validador)
validador = ( idade >= 18) # maior ou igual que
print(validador)
validador = ( idade <= 18)# menor ou igual que


print(validador)

if validador:
    print('Maior')

validador = not True
validador = not False
validador = (idade>18 and idade<18) # isso non equisiste, mais retornaria false
validador = (idade>18 or idade==18) # True pois OR siginifica uma ou outra verdadadeira


