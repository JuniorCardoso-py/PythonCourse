lista = list(range(5,25))
print(lista) # imprimir tudo q tem dentro da lista
print(lista[10]) # imprimir somente o elemento na posição 10 da lista
print(lista[10:15]) # imprimir Do elemento 10 ao 14 da lista
print(lista[10:16]) # imprimir do elemento 10 ao 15 da lista
print(lista[-1]) # imprimir do primeiro ao ultimo elemento da lista
print(lista[10:20:3]) # imprimir do elemento 10 ao 20 pulando de 3 em 3 elementos
print(lista[10:]) # imprimir do elemento 10 ao final da lista

lista = [3,4,5,[9,10,11],20,30]
print(lista[3][0])
lista = [3,4,5,[9,[80,90,100,[200,300,400]],11],20,30]
print(lista[3][1][3][2])
print(lista[3][1][3][1])
print(lista[3])
print(lista[3][1])
print(lista[3][1][3])
print(lista[3][1][3][1])

for i in range(10):
    print(i)

def mostrar (numero):
    for i in range(numero):
        print(i)

mostrar(5)