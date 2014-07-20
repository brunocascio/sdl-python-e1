# -*- coding: utf-8 -*-

# Se importan dependencias
import random, pickle

class Entrega(object):	
	
	def __init__(self, path="datos"):
		try:
			self.path = path
			fo = open(self.path, "rb")
			self.dictData = pickle.load(fo)
		except IOError:
			"""No existe el archivo, lo creo"""
			fo = open(self.path, "wb+")
			self.dictData = {}
		except EOFError:
			self.dictData = {}
		fo.close()

	def __save(self):
		"""Persiste la información"""
		fo = open(self.path, "wb")
		pickle.dump(self.dictData,fo)
		fo.close()

	"""
		Operaciones con Categorias
	"""


	def pruebas (self):
		return self.dictData


	def categories(self):
		"""Retorna una lista con todas las categorias ordenadas alfabeticamente"""
		return (sorted(self.dictData.keys()))

	
	def addCategory(self, category):
		"""Agrega una nueva categoria
		    Args:
		        category: El nombre de la categoría
		    Returns: None"""
		if (category in self.dictData):
			print ("La categoría ingresada ya existe.")
		else:
			self.dictData[category] = {}
			self.__save()
	
	def addLevel (self, difficulty, category):
		"""Agrega un nuevo nivel a la categoría ingresada
			Args:
				difficulty: tipo entero, representa al nuevo nivel.
				category: categoría a la cual se agrega nivel
		"""
		try:
			self.dictData[category] = dictLevel
			if (difficulty in dictLevel):
				print ("El nivel ya existe en la categoría " + category + ".")
			else:
				dictLevel[difficulty] = {}
				self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")


	def addInfo (self, category, name, difficulty, result, description):
		"""Agrega información al archivo:
			Args: 
				category: nombre de la categoría
				difficulty: nivel de dificultad
				name: nombre de la nueva palabra 
				result: lista con los posibles anagramas
				description: breve descripción del elemento agregado.
		"""
		try:
			dictLevel= self.dictData[category]
			try:
				dictNames = dictLevel[difficulty]
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


	def infoCategoryLevelName (self, category, level, name):
		"""Retorna la información (lista de anagrama, descripción) referente a un nombre dado, nivel y categoría en un diccionario
			Returns: dict
		"""
		try:
			return self.dictData[category][level][name]
		except KeyError:
			#Debería tratar las claves por separado:
			print ("Surgió un error")


	def removeCategory(self, category):
		"""Remueve una nueva categoria
		    Args:
		        category: El nombre de la categoría
		    Returns: None"""
		try:
			self.dictData.pop(category)
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
			self.dictData[newCategory] = self.dictData.pop(category)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")



	"""
		Operaciones con palabras
	"""


	def wordsByCategoryNameDifficulty(self, category, difficulty):
		"""
			Retorna todas las palabras de una categoria en un determinado nivel de dificultad:
			Returns: list.
		"""
		try:
			return (sorted (self.dictData[category][difficulty].keys()))
		except KeyError:
			print ("La categoría ingresada no existe.")


	def wordByCategoryName(self, category, difficulty):
		"""
			Retorna una palabra aleatoria de una categoria en un determinado nivel.
			Returns: string.
		"""
		try:
			l = sorted (self.dictData[category][difficulty].keys())
			index = random.randint(1, len(l)) -1
			return (l[index])
		except KeyError:
			print ("La categoría ingresada no existe.")			

	
	def addAnagram(self,category,name, ana, difficulty):
		"""
		Agrega un anagrama a una determinada categoria en una determinada dificultad de name:
		    Args:
		        category: Categoria a la cual se le asignará la palabra
		        ana: Palabra a agregar
		        name: palabra a la cual se agrega el anagrama
		        difficulty : nivel en el cual se agrega palabra
		    Returns: None
		"""
		try:
			if not (ana in self.dictData[category][difficulty][name]["res"]):
				self.dictData[category][difficulty][name]["res"].append(ana)
				self.__save()
			else:
				print ("La palabra ingresada ya se encuentra en la lista de anagramas de " + name + ".")
		except KeyError:
			print ("La categoría ingresada no existe.")
		

	def removeName(self,category,name, difficulty):
		"""Remueve una palabra de una determinada categoria en un determinado nivel junto a toda su información:
		    Args:
		        category: Categoria de la palabra
		        name: Palabra a eliminar
		        difficulty: nivel de dificultad
		    Returns: None"""
		try:
			self.dictData[category][difficulty].pop(name)
			self.__save()
		except KeyError:
			print ("La palabra ingresada no existe.")
		except ValueError:
			print ("La palabra ingresada no existe en la categoría " + category + ".")
		

	def renameWord(self,category,name,newName, difficulty):
		"""
			Renombra una palabra de una determinada categoria
		    Args:
		        category: Categoria de la palabra
		        word: Palabra a modificar
		        newWord: NuevaPalabra
		    Returns: None
		"""
		try:
			self.dictData[category][difficulty][newName] = self.dictData[category][difficulty].pop(name)
			self.__save()
		except KeyError:
			print ("La categoría ingresada no existe.")
		except ValueError:
			print ("La palabra buscada no existe en la categoría " + category + ".")
