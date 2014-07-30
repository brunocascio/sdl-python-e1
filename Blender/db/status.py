# -*- coding: utf-8 -*-

import pickle
import os

class Status ():

	def __init__ (self, filename = "status"):
		self.path = os.path.dirname(os.path.abspath(__file__))
		try:
			self.path += '/'+filename
			fo = open(self.path, "rb")
			self.__dictData = pickle.load(fo)
		except (IOError, EOFError):
			"""No existe el archivo, lo creo"""
			fo = open(self.path, "wb+")
			self.__dictData = 	{"info":{
										"scoreMax": 0,
										"nivelActual": 1,
										"scoreActual": 0,
										"vidas": 3,
										}
								}
		fo.close()


	def __save(self):
		"""Persiste la información"""
		fo = open(self.path, "wb")
		pickle.dump(self.__dictData,fo)
		fo.close()


	def pruebas (self):
		return self.__dictData


	"""
		OPERACIONES CON LA INFORMACIÓN:

		GETTERS
	"""

	def getScoreMax (self):
		return (self.__dictData["info"]["scoreMax"])


	def getNivelActual (self):
		return (self.__dictData["info"]["nivelActual"])


	def getScoreActual (self):
		return (self.__dictData["info"]["scoreActual"])


	def getVidas (self):
		return (self.__dictData["info"]["vidas"])


	"""
		SETTERS
	"""

	def setScoreMax (self, scoreMax):
		self.__dictData["info"]["scoreMax"] = scoreMax
		self.__save()


	def setNivelActual (self, nivelActual):
		self.__dictData["info"]["nivelActual"] = nivelActual
		self.__save()


	def setScoreActual (self, scoreActual):
		self.__dictData["info"]["scoreActual"] = scoreActual
		self.__save()


	def setVidas (self, vidas):
		self.__dictData["info"]["vidas"] = vidas
		self.__save()



		
