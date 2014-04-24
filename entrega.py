#/usr/bin/env python3
# -*- coding: utf-8 -*-

#importaciones
import pickle
import random



class Entrega(object):	
	"""Clase Entrega"""

	def __init__(self):
		try:
			fo = open("datos", "rb")
			self.dictData = pickle.load(fo)
		except IOError:
			fo = open("datos", "wb+")
			self.dictData = {}
			self.dictData = pickle.dump(self.dictData, fo)
		fo.close()


	def __save(self):
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

	def __str__(self):
		self.all


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
		self.__save()


	def removeCategory(self, name):
		"""Remueve una nueva categoria
		    Args:
		        name: El nombre de la categoría
		    Returns: None"""
		self.dictData.pop(name,None)
		self.__save()


	def renameCategory(self, name, newName):
		"""Renombra una categoria
		    Args:
		        name: El nombre de la categoría a renombrar
		        newName: El nuevo nombre de la categoría
		    Returns: None"""
		self.dictData[newName] = self.dictData.pop(name)
		self.__save()



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
		self.__save()


	def removeWord(self,category,word):
		"""Remueve una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a eliminar
		    Returns: None"""
		list = self.dictData[category]
		list.pop(list.index(word));
		self.__save()


	def renameWord(self,category,word,newWord):
		"""Renombra una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a modificar
		        newWord: NuevaPalabra
		    Returns: None"""
		list = self.dictData[category]
		list[list.index(word)] = newWord;
		self.__save()