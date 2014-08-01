import entrega
import pprint

e = entrega.Entrega("datos")

def showMenu ():
	print()
	print ("1. Agregar palabra.")
	print ("2. Modificar palabra.")
	print ("3. Eliminar palabra. ")
	print ("4. Obtener diccionario palabra. (?)")
	print ("5. Renombrar categoría.")
	print ("6. Remover categoría.")
	print ("7. Mostrar todos los datos.")
	print ("8. Crear niveles.")
	print ("9. Crear datos de prueba.")
	#print ("8. Mostrar estado de juego.")
	print()
	print ("0. 	Salir")
	print()


print("====================================")
print("=========== Bienvenido =============")
print("====================================")
showMenu()
i = -1

while i != 0:
	
	#showMenu ()

	i = int( input ("Ingrese una opción: ") )
	if i == 1:
		pal = input ("Ingrese una palabra: ")
		cat = input ("Ingrese una categoría: ")
		desc = input ("Ingrese una descripción de la palabra: ")
		level = int (input ("Ingrese el nivel: "))
		try:
			e.addWord (level, cat, pal, desc)
		except Exception as e:
			print(e)
	elif i == 2:
		cat = input("Nombre de la categoría: ")
		name = input ("Ingrese el nombre que quiere modificar: ")
		rename = input ("Ingrese nuevo nombre: ")
		level = int (input ("Ingrese nivel: "))
		e.renameWord (cat, name, rename, level)
	elif i == 3:
		cat = input("Ingrese categoría: ")
		name = input ("Ingrese nombre que desea eliminar: ")
		level = int (input ("Ingrese nivel: "))
		e.removeWord (cat, name, level)
	elif i == 4:
		level = int (input ("Ingrese nivel: "))
		print (e.getWord (level))
	elif i ==5:
		cat = input("Nombre de la categoría que desea modificar: ")
		newCat = input ("Nombre nuevo de la categoría: ")
		level = int (input ("Ingrese nivel: "))
		e.renameCategory (cat, newCat, level)
	elif i == 6:
		cat = input("Nombre de la categoría que desea eliminar: ")
		level = int (input ("Ingrese nivel: "))
		e.removeCategory (cat, level)
	elif i == 7:
		pp = pprint.PrettyPrinter(depth=7)
		pp.pprint(e.showFullData())
	elif i == 8:
		ini = int (input("Ingrese nivel de comienzo: "))
		fin = int (input("Ingrese nivel de fin: "))
		for i in range (ini, fin + 1):
			e.addLevel(i)
	elif i == 9:
        	e.testData()
	elif i == 0:
		pass
	else:
		print("La opción ingresada no es válida")

exit()
