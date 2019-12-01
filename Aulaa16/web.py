#--- Importação da classe e funções do flask
#--- Primeiro informando para a instrução 'from' de qual módulo será importado
#--- Depois informando cada classe e função do flask que será utilizada
from flask import Flask, render_template, redirect, request
#--- Importação das funções para manipulação de faixa musical que foram cridas no arquivo 'faixa'
from faixa import ler_faixas, criar_faixa, salvar_faixa

#--- Criação de uma variável e feita atribuição da classe Flask
app = Flask(__name__)

#--- Criação de uma rota que responda ao endereço principal da aplicação web '/'
#--- A rota ao ser acessada irá chamar a função 'inicio()' 
#--- A função retornará um arquivo HTML através da função do flask 'render_template()'
#--- O arquivo HTML que será retornado esta localizado na pasta 'templates' dentro da pasta desta aula
#--- Além do nome do arquivo html passado para função 'render_template()' tambem passamos uma string
#--- A string passada foi nomeada de 'nome' e está poderá ser acessada no html 'inicio.html' utilizando código python
@app.route('/')
def inicio():
    return render_template("inicio.html", nome = 'Lista de Faixas')

#--- Criação de uma rota que responda ao de listagem de faixas '/lista'
#--- A rota ao ser acessada irá chamar a função 'listar_faixas()' 
#--- A função retornará um arquivo HTML através da função do flask 'render_template()'
#--- O arquivo HTML que será retornado esta localizado na pasta 'templates' dentro da pasta desta aula
#--- Além do nome do arquivo html passado para função 'render_template()' tambem passamos uma string
#--- A string passada foi nomeada de 'nome' e está poderá ser acessada no html 'inicio.html' utilizando código python
#--- Outro dado passado é o retorno da função 'ler_faixas()'
#--- Esta função retorna uma lista de dicionários que representam as faixas musicais salvas
#--- Este retorno foi nomeado de 'lista' que poderá ser acessado no html através de código Python
@app.route('/lista')
def listar_faixas():
    return render_template("lista.html", nome = 'Lista de Faixas', lista=ler_faixas())

#--- Rota criada para receber os dados enviados pelo formulario contido no arquivo html 'inicio.html'
#--- O arquivo 'inicio.html' é retornado pela rota principal '/' e função 'inicio()''
#--- Esta rota responde ao endereço '/salvar''
#--- Ao enviar os dados do formulario para o endereço '/salvar' a função 'salvar()' é chamada
#--- Cada dado enviado do formulário é recuperado na função com o auxilio da função do Flask 'request''
#--- A função 'request' possui um dicionário de nome args que contém os dados do formulário enviado
#--- As chaves do dicionário 'args' são baseadas na propriedade 'name' contida nos input html do formulário
#--- Após a leitura dos dados do formulário é chamada a função 'criar_faixa()' e enviado os dados da faixa por parâmetro
#--- A função 'criar_faixa()' retorna um dicionário que é passado como argumento para a função 'salvar_faixa()' que salva os dados em arquivo texto
#--- Por fim, na última linha é feito um redirecionamento para a rota da lista '/lista' 
#--- Fazendo com que a lista atualizada de faixas musicais seja apresentada ao usuário
@app.route('/salvar')
def salvar():
    musica = request.args['musica']
    album = request.args['album']
    artista = request.args['artista']
    faixa = criar_faixa(musica, album, artista)
    salvar_faixa(faixa)
    return redirect('/lista')

#--- Chama a função 'run()' do Flask que sobe um servidor web local para que a aplicação seja disponibilizada 
#--- Em um endereço e porta acessíveis por um navegador web (http://127.0.0.1:5000)
app.run()