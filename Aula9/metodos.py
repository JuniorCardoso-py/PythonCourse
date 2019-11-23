# Aula 9 - 19-11-2019
# --- Web 2
# Crie um programa que:
#--- 1- Leia dois numeros inteiros
#--- 2- Calcule a soma entre os dois numeros atraves de um metodo
#--- 3- Calcule a subtração entre dois numeros atraves de um metodo
#--- 4- Calcule a mutiplciação entre dois numero atraves de um metodo
#--- 5- Calcule a divisão inteira entre dois numeros atraves de um metodo
#--- 6- Calcule a divisão fracionada entre dois numeros atraves de um metodo
#--- 7- Calcule resto da divisão entre os dois numeros atraves de um metodo
#--- 8- Calcule a raiz entre dois numeros atraves de um metodo
#--- 9- Separe os metodos em outro arquivo

def soma (n1, n2):
    total1 = n1 + n2
    print(f'A soma entre os dois numeros é ')
    return total1
def subtração (n1, n2):
    total2 = n1 - n2
    print(f'A subtração entre os dois numeros é ')
    return total2
def mutiplicação (n1, n2):
    total3 = n1 * n2
    print(f'A mutiplicação entre os dois numeros é ')
    return total3
def divisão_inteira (n1, n2):
    total4 = n1 / n2
    print(f'A divisão inteira entre os dois numeros é ')
    return total4 
def divisão_fracionada (n1, n2):
    total5 = n1 // n2
    print(f'A divisão fracionada entre os dois numeros é ')
    return total5
def resto_da_divisão (n1, n2):
    total6 = n1 % n2
    print(f'A resto da divisão entre os dois numeros é ')
    return total6
def raiz (n1, n2):
    total7 = n1**(1/n2)
    print(f'A raiz entre os dois numeros é ')
    return (total7)