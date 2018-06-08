# CREATE TABLE noticia (
# 	id serial primary key,
# 	titulo text,
# 	descricao text,
# 	lixeira boolean
# );

class Noticia:
	def __init__(self, titulo = "", descricao = "", assunto = "", data = "", lixeira = False, id = 0):
		self.titulo = titulo
		self.descricao = descricao
		self.assunto = assunto
		self.data = data
		self.lixeira = lixeira
		self.id = id
	def __repr__(self):
		return str(self.id) + ";" + self.titulo + ";" + self.descricao	+ ";" + self.assunto + ";" + self.data	

class NotComentarioicia:
	def __init__(self, texto ="", data = "", lixeira = False, id = 0):
		self.titulo = titulo
		self.descricao = descricao
		self.assunto = assunto
		self.data = data
		self.lixeira = lixeira
		self.id = id
	def __repr__(self):
		return str(self.id) + ";" + self.titulo + ";" + self.descricao	+ ";" + self.assunto + ";" + self.data	