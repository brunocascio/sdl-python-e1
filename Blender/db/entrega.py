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
		config = {  
			1:{"coord":
				{"camara":0.28068, "personaje":-23.56558}},
			2:{"coord":
				{"camara":73.81065, "personaje":49.96439}},
			3:{"coord":
				{"camara": 130.39062, "personaje": 106.54436}},
			4:{"coord":
				{"camara": 192.06549, "personaje": 168.21923}},
			5:{"coord":
				{"camara": 258.99521, "personaje": 235.14895}}
		}

		teclas = {
			"arriba"		: 146,
			"abajo"			: 144,
			"izquierda"		: 143,
			"derecha"		: 145,
			"lanzar"		: 100,
			"soltar"		: 32,
			"ayuda_juego"	: 162,
			"ayuda_palabra"	: 163
		}

		self.dictData = {"config": config, "globales": { "teclas": teclas }, "datos":{}}


	def getTeclas(self):
		return self.dictData["globales"]["teclas"]


	def setTeclas(self, dict):
		self.dictData["globales"]["teclas"] = dict
		self.__save()


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
			print ("La palabra ingresada no existe en la categoría ingresada.")
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


	def addWord (self, level, category, name, descr):
		"""
			Crea una nueva palabra en la escructura de datos.
			Args:
				level: nivel donde se agregará palabra.
				category: categoría donde se guardará la palabra ingresada (si no existe, se crea).
				name: palabra.
				descr: breve descripción de la palabra ingresada.
		"""
		if not (category.lower() in self.dictData["datos"][level]):
			self.dictData["datos"][level][category.lower()] = {}
		if len(name) != (4 + level-1):
			raise Exception("Para el nivel "+str(level)+" debe ingresar una palabra de "+str(4+level-1)+" letras")
		self.dictData["datos"][level][category.lower()][name.lower()] = descr	
		self.__save()
		

	"""
		OPERACIONES CON ANAGRAMAS (NOMBRE, CATEGORÍA Y NIVEL CONOCIDOS)
	"""


	def getWord (self, level):
		"""
			- Retorna una estructura con la categoria de la palabra, la palabra en si y su descripción, de forma aleatoria, de un nivel dado (1..5).
			Ejemplo -> {category:'peces',value:'tiburon',descripcion:"es carnívoro"}
			- Una excepción ocurre si el nivel se encuentra fuera del rango o el nivel está vacío (no puede seguir jugando).
			Returns:
				diccionario.
		"""
		l = list (self.dictData["datos"][level].keys())
		if (len (l) != 0):
			cat = l[random.randint (0, len (l) -1 )]
			#
			l2 = list (self.dictData["datos"][level][cat].keys())
			nombre = l2[random.randint(0, len (l2) -1)]
			return ({cat: { nombre : self.dictData["datos"][level][cat][nombre]}})
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


	"""
	    OPERACIONES AUTOMÁTICAS
	"""

	def reinitialize(self):
		self.__inicializarDatos()
		self.__save()

	def testData(self):
		self.dictData["datos"] = {
	        1: {'animales':{
	                        'gato' : 'Les gusta dormir',
	                        'leon' :  'Es el rey de la selva',
						    'rata' :  'Estan en la basura y tienen cola larga.',
						    'pato' : 'Tienen un pico muy largo.'
	                       },
	            'utiles':{
	                      'goma'   : 'Se usa para borrar'  
	                     },
	            'flores':{
	                      'rosa'   : 'Su nombre es el mismo que un color'
	                     },
	            'frutas':{
	                      'pera'   : 'Es de color amarillo y jugosa'
	                     },
	             'verduras':{
						     'papa': 'Se pueden cocinar fritas o hacer pure.'
							},
	            'transporte':{
	                         'auto': 'Tiene 4 ruedas'
	                         }
	           },
	        2: {
	            'utiles':{
	                      'lapiz'    : 'Se usa para escribir y dibujar',
						 },
	            'animales':{
						  'perro': 'Mejor amigo del hombre',
	                      'tigre': 'Tiene muchas manchas',
	                      'raton': 'Le gusta el queso (no pone plata cuando hay que pagar)'
						 },
	            'peces': {
	                      'tiburon': 'Es carnívoro',
	                      'ballena': 'Es muy grande',
	                     },
	             'frutas':{
	                      'limon'  : 'De color amarillo y acido.'
						  },
				 'transporte':{
	                          'micro': 'Puede llevar a muchas personas.',
	                          'avion': 'Vuela, transporta pasajeros.'
				              }
	           },
	        3: {
	            'verduras':{
	                      'tomate': 'Es de color rojo',
	                      'morron': 'Es de color rojo o verde',
						  'pepino': 'Color verde y largo'
	                     },
	            'peces': {
	                      'payaso' : 'El pez de buscando a Nemo era un pez ...... ',
	                      'espada' : 'Tiene nariz larga y puntiaguda, es un pez......',
						  'anchoa' : 'Se puede poner sobre la pizza.'
	                     },
	            'transporte':{
	                          'camion': 'Utilizados para transportar carga.'
	                         },
	            'plantas':{
	                       'cactus': '¡OJO! Tiene espinas.'
	                      },
	             'frutas':{
	                      'banana' : 'Alimento preferido de los monos',
	                      'sandia' : 'Verde por fuera, rojo por dentro',
	                      'pomelo' : 'Es muy ácido, pero rico; algunos son rosados por dentro.',
	                      'cereza' : 'De color roja, se le ponen a los postres.'
						  },
				'animales':{
	                      'jirafa' : 'Tiene el cuello muy largo y come hojas.'
						   }
	           },
	        4: {
	            'flores':{
	                      'girasol'  : 'Sus semillas pueden comerse'
	                     },
	            'animales':{
	                      'tortuga'  : 'Es un animal muy lento.'
	                       },
	            'verduras':{
	                      'lechuga'  : 'Comida preferida de las tortugas',
	                      'cebolla'  :  'Hace llorar a quien la corta.'
	                     },
	             'peces' :{
	                      'tiburon'  : 'Es carnívoro',
	                      'ballena'  : 'Es muy grande'
						  },
				 'frutas':{
	                      'naranja'  : 'Tiene el mismo nombre que un color',
	                      'manzana'  : 'Pueden ser de color verde o rojas.'
						  }
	           },
	        5: {
				'utiles'    :{
							  'lapicera' : 'Existen de varios colores, por lo general, azules',
							 },
	            'transporte':{
	                          'camioneta': 'Son todo terreno',
	                          'bicicleta': 'Cuenta con 2 ruedas',
	                          'motocicleta': 'Cuenta con 2 ruedas y un motor'
	                         },	
	            'animales':{
	                        'hipopotamo': 'Les gusta permanecer en el lodo',
	                        'cocodrilo' : 'De color verde. ¡No lo hagas enojar!',
	                        'camaleon'  : 'Puede cambiar de color.'
	                       },
	            'verduras':{
	                        'berenjena': 'Es de color violeta.',
							'zanahoria': 'Comida preferida de los conejos'
	                       }
	           }
	    }
		self.__save()
