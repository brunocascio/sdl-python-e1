# -*- coding: utf-8 -*-

import random
import pickle
import os

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


	def pruebas (self):
		return self.dictData


	"""
		OPERACIONES CON CATEGORÍAS
	"""

	def categories(self):
		"""Retorna una lista con todas las categorias ordenadas alfabeticamente"""
		return (sorted(self.dictData["datos"].keys()))

	
	def addCategory(self, category):
		"""Agrega una nueva categoria
		    Args:
		        category: El nombre de la categoría
		    Returns: None"""
		if (category in self.dictData["datos"]):
			print ("La categoría ingresada ya existe.")
		else:
			self.dictData["datos"][category] = {}
			self.__save()


	def removeCategory(self, category):
		"""Remueve una nueva categoria
		    Args:
		        category: El nombre de la categoría
		    Returns: None"""
		try:
			self.dictData["datos"].pop(category)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	def renameCategory(self, category, newCategory):
		"""Renombra una categoria
		    Args:
		        category: El nombre de la categoría a renombrar
		        newCategory: El nuevo nombre de la categoría
		    Returns: None"""
		try:
			self.dictData["datos"][newCategory] = self.dictData.pop(category)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	"""
		OPERACIONES CON NIVELES.
	"""
	

	def addLevel (self, level, category):
		"""Agrega un nuevo nivel a la categoría ingresada.
			Args:
				level: tipo entero, representa al nuevo nivel.
				category: categoría a la cual se agrega nivel
		"""
		try:
			"""Obtengo el diccionario de determinada categoría"""
			dictCat =self.dictData["datos"][category]
			if (level in dictCat):
				print ("El nivel ya existe en la categoría " + category + ".")
			else:
				dictCat[level] = {}
				self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	"""
		OPERACIONES CON NOMBRES (DADOS UNA CATEGORÍA Y UN NIVEL ESPECÍFICOS)
	"""


	def wordsByCategoryNameDifficulty(self, category, level):
		"""
			Retorna todas las palabras de una categoria en un determinado nivel de dificultad:
			Returns: list.
		"""
		try:
			return (sorted (self.dictData["datos"][category][level].keys()))
		except KeyError:
			print ("La categoría ingresada no existe.")


	def wordByCategoryName(self, category, level):
		"""
			Retorna una palabra aleatoria de una categoria en un determinado nivel.
			Returns: string.
		"""
		try:
			l = sorted (self.dictData["datos"][category][level].keys())
			index = random.randint(1, len(l)) -1
			return (l[index])
		except KeyError:
			print ("La categoría ingresada no existe.")		


	def removeName(self,category, name, level):
		"""Remueve una palabra de una determinada categoria en un determinado nivel junto a toda su información:
		    Args:
		        category: Categoria de la palabra
		        name: Palabra a eliminar
		        level: nivel de dificultad
		    Returns: None"""
		try:
			self.dictData["datos"][category][level].pop(name)
			self.__save()
		except KeyError:
			print ("La palabra ingresada no existe.")
		except ValueError:
			print ("La palabra ingresada no existe en la categoría " + category + " en el nivel " + level + ".")
		

	def renameWord(self, category, name, newName, level):
		"""
			Renombra una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a modificar
		        newWord: NuevaPalabra
		    Returns: None
		"""
		try:
			self.dictData["datos"][category][level][newName] = self.dictData["datos"][category][level].pop(name)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")
		except ValueError:
			print ("La palabra buscada no existe en la categoría " + category + ".")

	#Verificar unicidad dentro de la lista result antes de enviarla.
	def addInfo (self, category, name, level, result, description):
		"""Agrega información al archivo:
			Args: 
				category: nombre de la categoría
				level: nivel de dificultad
				name: nombre de la nueva palabra 
				result: lista con los posibles anagramas
				description: breve descripción del elemento agregado.
		"""
		try:
			dictCat= self.dictData["datos"][category]
			try:
				dictNames = dictCat[level]
				if (name in dictNames):
					print ("El nombre ingresado ya existe.")
				else:
					nombre = {}
					nombre["res"] = result
					nombre["descr"] = description
					dictNames[name] = nombre
					self.__save()
			except KeyError:
				print ("El nivel de dificultad ingresado no existe.")
		except KeyError:
			print ("La categoría ingresada no existe.")


	"""
		OPERACIONES CON ANAGRAMAS (NOMBRE, CATEGORÍA Y NIVEL CONOCIDOS)
	"""


	
	def addAnagram(self,category,name, ana, level):
		"""
		Agrega un anagrama a una determinada categoria en una determinada dificultad de name:
		    Args:
		        category: Categoria a la cual se le asignará la palabra
		        ana: Palabra a agregar
		        name: palabra a la cual se agrega el anagrama
		        level : nivel en el cual se agrega palabra
		    Returns: None
		"""
		try:
			#Antes de agregar anagrama, verifico unicidad.
			if not (ana in self.dictData["datos"][category][difficulty][name]["res"]):
				self.dictData["datos"][category][difficulty][name]["res"].append(ana)
				self.__save()
			else:
				print ("La palabra ingresada ya se encuentra en la lista de anagramas de " + name + ".")
		except KeyError:
			print ("La categoría ingresada no existe.")


	def renameAnagram (self, category, name, ana, level, newAna):
		"""
			Renombra un anagrama de la lista del nombre ingresado.
			Args:
				category: categoría donde se halla el anagrama.
				name: nombre al cual corresponde el anagrama.
				ana: palabra a modificar
				newAna: nombre nuevo.
			Returns:
				None
		"""
		try:
			l = self.dictData["datos"][category][level][name]["res"]
			if (ana in l):
				l.remove (ana)
				#Si el nuevo anagrama no estaba en la lista, lo agrego.
				if not (newAna in l):
					l.append (newAna)
		except KeyError:
			print ("Error de clave.")


	def removeAnagram (self, category, name, ana, level):
		"""
			Remueve un determinado anagrama de la lista del nombre ingresado.
			Args:
				category: categoría.
				name: nombre donde se busca anagrama.
				ana: anagrama a eliminar de la lista de nombres.
				level: nivel de dificultad donde se encuentra el nombre.
			Returns:
				None.
		"""
		try:
			#Obtengo la lista de anagramas
			l = self.dictData["datos"][category][level][name]["res"]
			if (ana in l):
				l.remove (ana)
		except KeyError:
			print ("Error de claves.")
			

	def anagrams (self, category, name, level):
		"""
			Retorna una lista de anagramas para determinada palabra.
			Args:
				category: nombre de categoría donde se encuentra palabra.
				name: nombre de la palabra de la cual se obtiene lista.
				level: nivel de dificultad
			Returns:
				Retorna lista de strings.
		"""
		try:
			return (self.dictData["datos"][category][level][name]["res"])
		except KeyError:
			print ("Tratar error de cada clave (category, difficulty y name) por separado.")


	def description (self, category, name, level):
		"""
			Retorna la descripción de una palabra en determinada categoría de determinado nivel de dificultad.
			Returns: string.
		"""
		try:
			return (self.dictData["datos"][category][level][name]["descr"])
		except KeyError:
			print ("Error de claves.")

	
	def infoCategoryLevelName (self, category, level, name):
		"""Retorna la información (lista de anagrama, descripción) referente a un nombre dado, nivel y categoría en un diccionario
			Returns:
				dict de dict.:
					"res" : lista de anagramas
					"descr" : descripcion.
		"""
		try:
			return self.dictData["datos"][category][level][name]
		except KeyError:
			#Debería tratar las claves por separado:
			print ("Error de claves.")


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



	
