#inicialização de uma variavel tipo lista
lista1 = []
#Inicialização de uma variavel lista com elementos
lista2 = ['Marcela', 'Nicole', '*Matheus']
#lista de inteiros
lista3 = [1,2,3,4,5]
#lista de tipos diferentes
lista4 = [1, "Junior", 12.5 ]


#impressão das listas criadas
print(lista1)
print(lista2)
print(lista3)

# ----- Adicionandos elementos em uma lista ja criada
lista1.append(lista1)
lista1.append(lista2)
lista1.append(lista3)
lista1.append(input('Qual sua idade?'))
print(lista1)

# ----- Criação de lista com dados vindos da função input
lista_pergunta = [input('Qual Seu numero favorito?'), input('Qual sua data de aniversario')]
print(lista_pergunta)
# ----- Recuperando um dado de uma posição especifica da lista
print(lista2 [2])
posicao = int(input('Qual posição: '))
print(lista2[posicao-1])


