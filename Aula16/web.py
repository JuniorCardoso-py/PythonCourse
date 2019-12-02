from flask import Flask, render_template
from teste import criar_faixa, ler_faixa, salvar_faixa
app = Flask(__name__)


@app.route('/lista')
def lista_listar_faixa():
    return render_template("lista.html", nome = 'Lista de Faixas')


app.run()