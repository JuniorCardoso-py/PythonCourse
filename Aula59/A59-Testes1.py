# testes em sucuri

#verificacao se determinada condição é verdadeira
# Checando se condições são verdadeiras
assert True
assert (10 == 10)
assert (10 > 5)
assert ('Voltolini' != 'Vinicius')

# Método pra uso no teste
def soma(n1, n2):
    resultado = n1 + n2
    return resultado
# Método com parâmetro opcional para uso no teste
def multiplicacao(n1, n2, n3=1):
    return n1 * n2 * n3

# Método com condicinal para uso no teste
def checa_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False
# teste de resultado do método soma
assert soma(5 , 10) == 15
# Teste de resultado do método de multiplicação
assert multiplicacao(2,4,6) == 48
# Teste de método de multiplicação com argumento opcional
assert multiplicacao(2,4) == 8
# Teste de metodo com a condicional if
assert checa_maioridade(18) == True
# Teste de metodo com a condicional if 2
assert checa_maioridade(19) == True
# Teste de metodo com a condicional else
assert checa_maioridade(17) == False



