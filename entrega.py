# -*- coding: utf-8 -*-
import random

import pickle

class Entrega(object):	
	
	def __init__(self):
		try:
			fo = open("datos", "rb")
			self.dictData = pickle.load(fo)
		except IOError:
			fo = open("datos", "wb+")
			self.dictData = {}
		except EOFError:
			self.dictData = {}
		fo.close()

	def __save(self):
		"""Persiste la información"""
		fo = open("datos", "wb")
		pickle.dump(self.dictData,fo)
		fo.close()

	"""
		Operaciones con Categorias
	"""

	def categories(self):
		"""Retorna una lista con todas las categorias ordenadas alfabeticamente"""
		return (sorted(self.dictData.keys()))

	
	def addCategory(self, name):
		"""Agrega una nueva categoria
		    Args:
		        name: El nombre de la categoría
		    Returns: None"""
		if (name in self.dictData):
			print ("La categoría ingresada ya existe.")
		else:
			self.dictData[name] = []
			self.__save()

	def removeCategory(self, name):
		"""Remueve una nueva categoria
		    Args:
		        name: El nombre de la categoría
		    Returns: None"""
		try:
			self.dictData.pop(name)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	def renameCategory(self, name, newName):
		"""Renombra una categoria
		    Args:
		        name: El nombre de la categoría a renombrar
		        newName: El nuevo nombre de la categoría
		    Returns: None"""
		try:
			self.dictData[newName] = self.dictData.pop(name)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")



	"""
		Operaciones con palabras
	"""

	def words(self):
		"""
			Retorna todas las palabras agrupadas por categorias
			Tanto las categorias como las palabras se encuentran ordenandas alfabeticamente
			Returns: diccionario.
		"""
		return {c: sorted(l) for (c,l) in sorted(self.dictData.items())}


	def wordsByCategoryName(self, category):
		"""
			Muestra todas las palabras de una categoria
			Returns: list.
		"""
		try:
			return (self.dictData[category])
		except KeyError:
			print ("La categoría ingresada no existe.")


	def wordByCategoryName(self, category):
		"""
			Retorna una palabra aleatoria de una categoria
		"""
		try:
			l = self.dictData[category]
			index = random.randint(1, len(l)) -1
			return (l[index])
		except KeyError:
			print ("La categoría ingresada no existe.")			


	def addWord(self,category,word):
		"""Agrega una palabra a una determinada categoria
		    Args:
		        category: Categoria a la cual se le asignará la palabra
		        word: Palabra a agregar
		    Returns: None"""
		try:
			if not (word in self.dictData[category]):
				self.dictData[category].append(word)
				self.__save()
			else:
				print ("La palabra ingresada ya se encuentra en la categoría " + category + ".")
		except KeyError:
			print ("La categoría ingresada no existe.")


	def removeWord(self,category,word):
		"""Remueve una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a eliminar
		    Returns: None"""
		try:
			list = self.dictData[category]
			list.pop(list.index(word))
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")
		except ValueError:
			print ("La palabra ingresada no existe en la categoría " + category + ".")
		

	def renameWord(self,category,word,newWord):
		"""Renombra una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a modificar
		        newWord: NuevaPalabra
		    Returns: None"""
		try:
			list = self.dictData[category]
			list[list.index(word)] = newWord
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")
		except ValueError:
			print ("La palabra buscada no existe en la categoría " + category + ".")
