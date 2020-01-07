idade = 23
salario = 5000.00
nome = 'Junior'
verdadeiro = True
falso = False

print('='*50, '\n')


print (idade)
print(salario)
print(nome)
print(verdadeiro)
print(falso)
print('\n', '='*50, sep="")

print(idade,salario,nome,verdadeiro,falso)

print('\n','\t','A minha idade é', idade, 'O meu salario é', salario, 'Meu nome é', nome, 'Verdadeiro =', verdadeiro, 'Falso', falso)

print('\n'*2, '='*50 )

print('\n','\t'*2, 'A minha idade é {} o meu salario é {} o meu nome é {} verdadeiro: {} Falso {} '.format(idade,salario,nome,verdadeiro,falso))

print('\n', '='*50)

print('\n','\t'*3, f'A minha idade é {idade} o meu salario é {salario} o meu nome é {nome} verdadeiro: {verdadeiro} Falso {falso} ')
# a forma acima se chama interpolação de string.
print('\n','='*50)