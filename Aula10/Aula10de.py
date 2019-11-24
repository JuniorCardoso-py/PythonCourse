# Aula 10 - 20 - 11 - 2019
#
#--- Web - Calculadora

from flask import Flask, render_template, request
from metodos import *
app= Flask(__name__)
nome_pagina = 'Calculadora'

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route("/calcular")
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    resultado = soma(n1,n2)
    result2 = mutiplicação(n1,n2)
    result3 = divisão_inteira(n1,n2)
    result4 = subtração(n1,n2)
    result5 = divisão_fracionada(n1,n2)
    result6 = raiz(n1,n2)
    result7 = resto_da_divisão(n1,n2)
    results = {'soma':resultado,'mutiplicação':result2,'divisão_inteira':result3, 'subtração':result4, 'divisão_fracionada':result5,'raiz':result6, 'resto_da_divisão':result7}
    return render_template('resultado.html', n1=n1, n2=n2, results=results)

app.run()