import entrega

e = entrega.Entrega("datos")

print("====================================")
print("=========== Bienvenido =============")
print("====================================")

print()
print("=========== Categorias ===========")
print()
print ("1. 	Listar Categorías")
print ("2. 	Agregar Categoría")
print ("3. 	Modificar Categoría")
print ("4. 	Eliminar Categoría")

print()
print("=========== Palabras ===========")
print()
print ("5.  Listar Palabras")
print ("6.  Listar Palabras de una Categoría")
print ("7.  Obtener una Palabra de una Categoría")
print ("8.  Agregar Palabra a una Categoría")
print ("9.  Modificar Palabra de una Categoría")
print ("10. Eliminar Palabra de una Categoría")

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
	elif i == 5:
		print (e.words())
	elif i == 6:
		cat = input("Nombre de la categoría: ")
		print (e.wordsByCategoryName(cat))
	elif i == 7:
		cat = input("Nombre de la categoría: ")
		print (e.wordByCategoryName(cat))
	elif i == 8:
		cat = input("Nombre de la categoría: ")
		word = input("Palabra: ")
		e.addWord(cat,word)
	elif i == 9:
		cat = input("Nombre de la categoría: ")
		word = input("Palabra a modificar: ")
		newWord = input("Palabra a agregar: ")
		e.renameWord(cat,word,newWord)
	elif i == 10:
		cat = input("Nombre de la categoría: ")
		word = input("Palabra a eliminar: ")
		e.removeWord(cat,word)
	elif i == 0:
		pass
	else:
		print("La opción ingresada no es válida")

exit()
