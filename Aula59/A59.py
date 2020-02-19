#---- Metodos
# --- Argumentos Ordenados
# --- Argumentos Nomeados
# --- Argumentos Opcionais

# Método para uso de parametros ordenados
def soma(n1, n2):
    resultado = n1 + n2
    return resultado
# Chamada de metodo com argumentos nomeados
res = soma(10,20)
print(res)

# Método para chamada de parâmetros nomeados
def subtracao(n1, n2, n3):
    resultado = n1 - n2 - n3
    return  resultado

# Chamada de método com argumentos nomeados
res2 = subtracao(n3=10 ,n2=20, n1=10)
print(res2)

# Método para para uso de parâmetros opcionais
def multiplicacao(n1, n2, n3=1):
    return n1 * n2 * n3

# Chamada de método com uso de argumento opcional
res3 = multiplicacao(10, 20)
print(res3)

