import psycopg2
from modelo import *

class Conexao:
	def abre(self):
		self.conexao = psycopg2.connect("dbname=keep user=postgres password=postgres host=localhost")
		self.cursor = self.conexao.cursor()

	def encerra(self):
		self.conexao.close()
		self.cursor.close()


class NoticiaDAO:

	def adicionar(self, noticia):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("INSERT INTO noticia (titulo, descricao, assunto, data) VALUES(%s, %s, %s, %s);", [noticia.titulo, noticia.descricao, noticia.assunto, noticia.data])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	# se False (padrao) = lista as anotacoes que nao estao na lixeira
	# se True = lista as anotacoes da lixeira
	def listar(self, lixeira = False):
		conexao = Conexao()
		conexao.abre()
		conexao.cursor.execute("SELECT * FROM noticia WHERE lixeira = %s", [lixeira])
		vet = conexao.cursor.fetchall()
		# print "======================"
		# print vet
		# print "======================"
		vetNoticia = []
		for a in vet:
			# titulo, descricao, lixeira, id
			vetNoticia.append(Noticia(a[1], a[2], a[3], a[4], a[5], a[0]))
		conexao.encerra()
		return vetNoticia
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("DELETE FROM noticia WHERE id = %s", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	def alterar(self, noticia):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE noticia SET titulo = %s, descricao = %s, assunto = %s, data = %s WHERE id = %s;", [noticia.titulo, noticia.descricao, noticia.assunto, noticia.data,noticia.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()	
		
	def obter(self, id):
		conexao = Conexao()
		conexao.abre()
		conexao.cursor.execute("SELECT * FROM noticia WHERE id = %s", [id])
		a = conexao.cursor.fetchone()
		noticia = Noticia(a[1], a[2], a[3], a[4], a[5], a[0])
		conexao.encerra()
		return noticia
	def replicar(self, id):
		noticiaAux = self.obter(id)
		noticiaAux.id = 0
		self.adicionar(noticiaAux)
	def lixeira(self, id, lixeira = True):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE noticia SET lixeira = %s WHERE id = %s;", [lixeira, id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

class comentarioDAO:

	def adicionar(self, comentario):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("INSERT INTO comentario (texto, data) VALUES(%s, %s);", [comentario.texto, comentario.data])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	def listar(self, lixeira = False):
		conexao = Conexao()
		conexao.abre()
		conexao.cursor.execute("SELECT * FROM comentario WHERE lixeira = %s", [lixeira])
		vet = conexao.cursor.fetchall()
		vetComentario = []
		for a in vet:
			vetComentario.append(Comentario(a[1], a[2], a[3], a[0]))
		conexao.encerra()
		return vetComentario