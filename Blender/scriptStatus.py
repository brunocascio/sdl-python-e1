# -*- coding: utf-8 -*-
import status

s= status.Status()

#Script para configurar archivo "status":

print ("Ingrese la opción deseada:")
print ()
print ("1. Set Nivel Actual")
print ("9. Imprimir estrucutura.")

print ("0. Salir")

i = -1

while (i !=0):
	i = int (input ("Ingrese una opción: "))
	if i == 1:
		nivel = int (input ("Ingrese el nivel actual: "))
		s.setNivelActual (nivel)
	elif i == 9:
		print (s.pruebas())
	elif i == 0:
		pass
	else:
		print ("Opción inválida.")
