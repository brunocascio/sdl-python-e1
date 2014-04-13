# -*- coding: utf-8 -*-

#importaciones
import pickle
import random


class Entrega(object):	


	def __init__(self):
		fo = open("datos", "rb")
		#self.dictData = {'idioma': ['hola','como','andas'], 'silabas': ['ma ña na', 'so lea do']}
		self.dictData = pickle.load(fo)
		#fo = open("datos", "wb")
		#pickle.dump(self.dictData,fo)
		fo.close()


	def _save(self):
		"""Persiste la información"""
		fo = open("datos", "wb")
		pickle.dump(self.dictData,fo)
		fo.close()


	def all(self):
		"""Muestra todas las categorias ordenadas alfabeticamente"""
		print()
		print('#### Contenido de la estructura ####')
		print()
		print(self.dictData)
		print()
		print('#### Contenido del archivo ####')
		print()
		fo = open("datos", "rb")
		print(pickle.load(fo))
		print()
		fo.close()



	"""
		Operaciones con Categorias
	"""

	def categories(self):
		"""Muestra todas las categorias ordenadas alfabeticamente"""
		print(sorted(self.dictData.keys()))

	
	def addCategory(self, name):
		"""Agrega una nueva categoria
		    Args:
		        name: El nombre de la categoría
		    Returns: None"""
		self.dictData[name] = []
		self._save()


	def removeCategory(self, name):
		"""Remueve una nueva categoria
		    Args:
		        name: El nombre de la categoría
		    Returns: None"""
		self.dictData.pop(name,None)
		self._save()


	def renameCategory(self, name, newName):
		"""Renombra una categoria
		    Args:
		        name: El nombre de la categoría a renombrar
		        newName: El nuevo nombre de la categoría
		    Returns: None"""
		self.dictData[newName] = self.dictData.pop(name)
		self._save()



	"""
		Operaciones con palabras
	"""

	def words(self):
		"""
			Muestra todas las palabras agrupadas por categorias
			Tanto las categorias como las palabras se encuentran ordenandas alfabeticamente
		"""
		for (c,l) in sorted(self.dictData.items()):
			print(c,sorted(l))


	def wordsByCategoryName(self, category):
		"""Muestra todas las palabras de una categoria"""
		print(self.dictData[category])


	def wordByCategoryName(self, category):
		"""Muestra una palabra aleatoria de una categoria"""
		l = self.dictData[category]
		index = random.randint(1, len(l)) -1
		print(l[index])


	def addWord(self,category,word):
		"""Agrega una palabra a una determinada categoria
		    Args:
		        category: Categoria a la cual se le asignará la palabra
		        word: Palabra a agregar
		    Returns: None"""
		self.dictData[category].append(word);
		self._save()


	def removeWord(self,category,word):
		"""Remueve una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a eliminar
		    Returns: None"""
		list = self.dictData[category]
		list.pop(list.index(word));
		self._save()


	def renameWord(self,category,word,newWord):
		"""Renombra una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a modificar
		        newWord: NuevaPalabra
		    Returns: None"""
		list = self.dictData[category]
		list[list.index(word)] = newWord;
		self._save()



	#################### MAIN ######################


a = Entrega()
a.all()
print()