# -*- coding: utf-8 -*-

import random
import pickle
import os
import pprint

class Entrega ():	
	
	
	def __init__(self, filename="datos"):
		self.path = os.path.dirname(os.path.abspath(__file__))
		try:
			self.path += '/'+filename
			fo = open(self.path, "rb")
			self.dictData = pickle.load(fo)
		except (IOError, EOFError):
			"""No existe el archivo, lo creo"""
			fo = open(self.path, "wb+")
			self.__inicializarDatos()
		fo.close()


	def __inicializarDatos (self):
		config = {  1:{"coord":
						{"camara":0.28068, "personaje":-23.56558}},
					2:{"coord":
						{"camara":73.81065, "personaje":49.96439}},
					3:{"coord":
						{"camara": 130.39062, "personaje": 106.54436}},
					4:{"coord":
						{"camara": 192.06549, "personaje": 168.21923}},
					5:{"coord":
						{"camara": 258.99521, "personaje": 235.14895}}}

		self.dictData = {"datos":{}, "config": config}


	def __save(self):
		"""Persiste la información"""
		fo = open(self.path, "wb")
		pickle.dump(self.dictData,fo)
		fo.close()


	def showFullData (self):
		return self.dictData


	"""
		OPERACIONES CON CATEGORÍAS
	"""


	def removeCategory(self, category, level):
		"""Remueve una nueva categoria junto a toda su información.
		    Args:
		        category: El nombre de la categoría
		        level: nivel donde se elimina categoría.
		    Returns: None
		 """
		try:
			self.dictData["datos"][level].pop(category.lower())
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	def renameCategory(self, category, newCategory, level):
		"""Renombra una categoria
		    Args:
		        category: El nombre de la categoría a renombrar.
		        newCategory: El nuevo nombre de la categoría.
		        level: nivel donde se encuentra la categoría a eliminar.
		    Returns: None
		"""
		try:
			self.dictData["datos"][level][newCategory.lower()] = self.dictData["datos"][level].pop(category.lower())
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	"""
		OPERACIONES CON NIVELES.
	"""
	

	def addLevel (self, level):
		"""Agrega un nuevo nivel a la información del diccionario.
			Args:
				level: tipo entero, representa al nuevo nivel.
		"""
		dictDatos = self.dictData["datos"]
		#Me aseguro de no sobreescribir si ya existe en el diccionario la clave "level", sino no hago nada:
		if not (level in dictDatos):
			dictDatos[level] = {}
			self.__save()
		

	"""
		OPERACIONES CON NOMBRES
	"""
	

	def removeWord(self,category, name, level):
		"""Remueve una palabra de una determinada categoria en un determinado nivel junto a toda su información, si categoría queda vacía se elimina de determinado nivel:
		    Args:
		        category: Categoria de la palabra
		        name: Palabra a eliminar
		        level: nivel de dificultad
		    Returns: None"""
		try:
			self.dictData["datos"][level][category.lower()].pop(name)
			#Si no queda elemento en diccionario de categoría, la elimino del nivel:
			if (len (self.dictData["datos"][level][category.lower()]) == 0):
				self.dictData["datos"][level].pop(category.lower())
			self.__save()
		except KeyError:
			print ("La palabra ingresada no existe.")
		except ValueError:
			print ("La palabra ingresada no existe en la categoría " + category + " en el nivel " + level + ".")
		

	def renameWord(self, category, name, newName, level):
		"""
			Renombra una palabra de una determinada categoria en un nivel dado.
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a modificar
		        newWord: NuevaPalabra
		        level: nivel.
		    Returns:
				None
		"""
		try:
			self.dictData["datos"][level][category.lower()][newName] = self.dictData["datos"][level][category.lower()].pop(name)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")
		except ValueError:
			print ("La palabra buscada no existe en la categoría " + category + ".")


	def addWord (self, level, category, descr):
		"""
			Crea una nueva palabra en la escructura de datos.
			Args:
				level: nivel donde se agregará palabra.
				category: categoría donde se guardará la palabra ingresada (si no existe, se crea).
				descr: breve descripción de la palabra ingresada.
		"""
		self.dictData["datos"][level][category.lower()] = descr
		self.__save()
		

	"""
		OPERACIONES CON ANAGRAMAS (NOMBRE, CATEGORÍA Y NIVEL CONOCIDOS)
	"""


	def getWord (self, level):
		"""
			- Retorna una estructura con la categoria de la palabra, la palabra en si y su descripción, de forma aleatoria, de un nivel dado (1..5).
			Ejemplo -> {category:'peces',value:'tiburon',descripcion:"es carnívoro"}
			- Una excepción ocurre si el nivel se encuentra fuera del rango.
			Returns:
				diccionario.
		"""
		l = list (self.dictData["datos"][level].keys()))
		if (len (l) != 0):
			cat = l[random.randint (0, len (l) -1 )]
			#Lista de diccionarios palabras, descripcion
			l2 = self.dictData["datos"][level][cat]
			return ({cat: l2[random.randint (0, len(l2) -1 )]})
		else:
			raise ValueError ("No data.")
		

	"""
		OPERACIONES CON CONFIGURACIÓN.
	"""

	def getCoord (self, level):
		"""
			Devuelve las coordenadas de determinado nivel de cámara y personaje.
			Returns: dict.
		"""
		try: 
			return (self.dictData["config"][level]["coord"])
		except KeyError:
			print("Número de nivel inválido")



	
