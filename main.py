
# importando a biblioteca flask
from flask import Flask
# habilitando o redirecionamento
from flask import abort, redirect, url_for
# importando a camada de persistencia, ou seja, os daos
from persistencia import *
# templates
from flask import render_template
# receber dados do formulario
from flask import request

# criando um objeto de Flask
app = Flask(__name__)

# definindo a rota index
@app.route('/')
def listar():
	noticiaDAO = NoticiaDAO()
	# return render_template("listar.html", vetNoticia = noticiaDAO.listar(), vetNoticiaLixeira = noticiaDAO.listar(True))
	return render_template("listar.html", vetNoticia = noticiaDAO.listar(), vetNoticiaLixeira = noticiaDAO.listar(True), nome = "Listagem...")

	# sem o uso de templates
	# o codigo fica misturado
	# retorno = "<table border='1'>"
	# vetNoticia = noticiaDAO.listar()
	# for a in vetNoticia:
	# 	retorno = retorno + "<tr> <td> <a href='/excluir/"+ str(a.id) +"'> Excluir </a> </td> <td> " + a.titulo + "</td> </tr>"
	# retorno = retorno + "</table>"
	# return retorno

@app.route("/excluir/<id>")
def excluir(id):
	noticiaDAO = NoticiaDAO()
	noticiaDAO.excluir(int(id))
	return redirect(url_for('listar'))

@app.route("/replicar/<id>")
def replicar(id):
	noticiaDAO = NoticiaDAO()
	noticiaDAO.replicar(int(id))
	return redirect(url_for('listar'))

@app.route("/enviar_lixeira/<id>")
def enviar_lixeira(id):
	noticiaDAO = NoticiaDAO()
	noticiaDAO.lixeira(int(id))
	return redirect(url_for('listar'))


@app.route("/restaurar_lixeira/<id>")
def restaurar_lixeira(id):
	noticiaDAO = NoticiaDAO()
	noticiaDAO.lixeira(int(id), False)
	return redirect(url_for('listar'))

@app.route('/tela_alterar/<id>')
def tela_alterar(id):	
    return render_template("tela_alterar.html", noticia = NoticiaDAO().obter(int(id)))

@app.route('/tela_adicionar')
def tela_adicionar():	
    return render_template("tela_adicionar.html")


@app.route('/alterar', methods=['POST'])
def alterar():	
	noticia = Noticia()
	# por input hidden
	noticia.id = int(request.form['id'])
	noticia.titulo = str(request.form['titulo'])
	noticia.descricao = str(request.form['descricao'])
	noticia.assunto = str(request.form['assunto'])
	noticia.data = str(request.form['data'])
	# print "====================="
	# print noticia
	# print "====================="
	noticiaDAO = NoticiaDAO()
	noticiaDAO.alterar(noticia)
	return redirect(url_for("listar"))


@app.route('/adicionar', methods=['POST'])
def adicionar():	
	noticia = Noticia()
	noticia.titulo = str(request.form['titulo'])
	noticia.descricao = str(request.form['descricao'])
	noticia.assunto = str(request.form['assunto'])
	noticia.data = str(request.form['data'])
	# print "====================="
	# print noticia
	# print "====================="
	noticiaDAO = NoticiaDAO()
	noticiaDAO.adicionar(noticia)
	return redirect(url_for("listar"))

# Como executa?

# Opcoes:

# 1) No terminal
# python main.py

# 2) No terminal:
# FLASK_APP=main.py FLASK_DEBUG=1 flask run

# Traduzindo o comando....
# Estou executando o arquivo main.py
# habilitei o debug

# startando....
if __name__ == '__main__':
	app.run(debug=True)