# CyclicRotation
#
# Uma matriz A consistindo de N inteiros é fornecida.
# A rotação da lista significa que cada elemento é deslocado para a direita por um índice,
# e o último elemento da lista é movido para o primeiro lugar.
# Por exemplo, a rotação da lista A = [3, 8, 9, 7, 6] é [6, 3, 8, 9, 7]
# (os elementos são deslocados para a direita por um índice e 6 é movido para o primeiro lugar).
#
# O objetivo é girar a matriz A K vezes; isto é, cada elemento de A será deslocado para o K tempo certo.
#
# Escreva uma função:
#
# solução def (A, K)
#
# que, dada uma lista A que consiste em N números inteiros e um número inteiro K,
# retorna a lista A girada K vezes.
#
# Por exemplo, dado
#
#     A = [3, 8, 9, 7, 6]
#     K = 3
#     
# a função deve retornar [9, 7, 6, 3, 8]. Foram realizadas três rotações:
#
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# Por outro exemplo, dado
#
#     A = [0, 0, 0]
#     K = 1
# a função deve retornar [0, 0, 0]
#
# Dado

lista = [1,2,3,4,5]

class Base:
    def rotacao(self, lista):
        self.lista = lista
        self.contador = len(lista)-1
        numero = int(input(('Quantas vezes você quer girar a lista? ')))
        while self.contador != 0:
            for a in self.lista, self.lista in range(numero):
                nova_lista = []
                elemento = lista[self.contador]
                nova_lista.append(elemento)
                if self.contador != 0:
                    self.contador = self.contador - 1
                else:
                    self.contador = len(lista)-1
                    print(f'Nova Lista: {nova_lista}')
            print(nova_lista)


show = Base()
show.rotacao(lista)




# class Matriz:
#     def rotação(self):
#         self.A = [3, 8, 9, 7, 6]
#         self.B = [1, 2, 3, 4]
#         self.lista = int(input('Digite qual lista vc quer\nlista 1 = [3, 8, 9, 7, 6]\nlista 2 = [1, 2, 3, 4]: '))
#         self.r = int(input('Digite o número que quer que aconteça a rotação: '))
#         if self.lista == 1:
#             self.lista  = self.A
#         elif self.lista == 2:
#             self.lista = self.B
#
#         for i in range(self.r):
#             self.lista.insert(0, self.lista[-1])
#             self.lista.pop()
#         print(self.lista)
#
#
#
#
#
#
#
#
# #user.name=GABRI
#
#
# m = Matriz()
# m.rotação()













