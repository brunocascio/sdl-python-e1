import entrega

e = entrega.Entrega("datos")

print("====================================")
print("=========== Bienvenido =============")
print("====================================")

print()
print("=========== CATEGORÍAS ===========")
print()
print ("1. 	Listar Categorías")
print ("2. 	Agregar Categoría")
print ("3. 	Modificar Categoría")
print ("4. 	Eliminar Categoría")

print()
print("=========== NOMBRES ===========")
print()
print ("5.  Obtener lista de Anagramas.")
#print ("5.  Listar Palabras")
print ("6.  Listar Palabras de una Categoría")
print ("7.  Obtener una Palabra de una Categoría")
print ("8.  Agregar Palabra a una Categoría")
#print ("9.  Modificar Palabra de una Categoría")
print ("9.  Cargar archivo")
print ("10. Eliminar Palabra de una Categoría")
print ("11. pruebas.")
print ("12. Agregar Anagrama")
print ("13. Agregar nivel")
print ("14. Descripción.")
print ("15. Modificar un anagrama.")
print ("16. Eliminar un anagrama.")

print ()
print ("================ CONFIGURACIONES=============")
print ()

print()
print ("0. 	Salir")
print()

i = -1

while i != 0:
	i = int( input ("Ingrese una opción: ") )
	if i == 1:
		print(e.categories())
	elif i == 2:
		cat = input("Nombre de la categoría: ")
		e.addCategory(cat)
	elif i == 3:
		cat = input("Nombre de la categoría a modificar: ")
		newCat = input("Nombre de la categoría nueva: ")
		e.renameCategory(cat,newCat)
	elif i == 4:
		cat = input("Nombre de la categoría a eliminar: ")
		e.removeCategory(cat)
#	elif i == 5:
#		print (e.words())
	elif i ==5:
		cat = input("Nombre de la categoría: ")
		dif = int (input ("Nivel de dificultad: "))
		pal = input ("Nombre de la palabra: ")
		print (e.anagrams(cat, pal, dif))
	elif i == 6:
		cat = input("Nombre de la categoría: ")
		dif = int (input ("dificultad: "))
		print (e.wordsByCategoryNameDifficulty(cat, dif))
	elif i == 7:
		cat = input("Nombre de la categoría: ")
		dif = int (input ("Nivel: "))
		print (e.wordByCategoryName(cat, dif))
	elif i == 8:
		cat = input("Nombre de la categoría: ")
		word = input("Palabra: ")
		dif = input ("nivel de dificultad: ")
		e.addWord(cat,word, dif)
	elif i == 9:
		cat = input ("Nombre de la categoría")
		name = input ("Nombre de la nueva Palabra: ")
		dif = int (input ("nivel de dificultad: "))	
		ana = input ("Anagramas de la Palabra: ")
		l = []
		while (ana != "0"):
			#Verifico unicidad dentro de la lista:
			if not (ana in l):
				l.append(ana)
			ana = input ("Anagramas de la Palabra: ")
		desc = input ("Agregue una breve descripción del elemento a ingresar: ")
		e.addInfo (cat, name, dif, l, desc)
	elif i == 10:
		cat = input("Nombre de la categoría: ")
		word = input("Palabra a eliminar: ")
		dif = int (input ("Nivel : "))
		e.removeName(cat,word, dif)
	elif i == 11:
		print (e.pruebas())
	elif i == 12:
		cat = input ("Ingrese categoría: ")
		dif = int (input("dificultad: "))
		ana = input ("Ingrese Anagrama: ")
		name = input ("Ingrese el resultado del Anagrama: ")
		e.addAnagram(cat,name, ana, dif)
	elif i == 13:
		cat = input ("Ingrese categoría: ")
		dif = int (input("dificultad: "))
		e.addLevel (dif, cat)
	elif i == 14:
		cat = input("Nombre de la categoría: ")
		dif = int (input ("Nivel de dificultad: "))
		pal = input ("Anagrama: ")
		print (e.description(cat, pal, dif))
	elif i == 15:
		cat = input("Nombre de la categoría: ")
		dif = int (input ("Nivel de dificultad: "))
		pal = input ("Nombre de la palabra del anagrama a modificar: ")
		ana = input ("Nombre del anagrama a modificar: ")
		newAna = input ("Nombre nuevo: ")
		renameAnagram (self, cat, pal, ana, dif, newAna)
	elif i == 16:
		cat = input("Nombre de la categoría: ")
		dif = int (input ("Nivel de dificultad: "))
		pal = input ("Nombre de la palabra del anagrama a eliminar: ")
		ana = input ("Nombre del anagrama a eliminar: ")
		removeAnagram (self, cat, pal, ana, dif)
	elif i == 0:
		pass
	else:
		print("La opción ingresada no es válida")

	"""elif i == 9:
		cat = input("Nombre de la categoría: ")
		word = input("Palabra a modificar: ")
		newWord = input("Palabra a agregar: ")
	e.renameWord(cat,word,newWord)"""

exit()
