import entrega
import pprint

e = entrega.Entrega()

def showMenu ():
	print()
	print ("1.  Agregar palabra.")
	print ("2.  Modificar palabra.")
	print ("3.  Eliminar palabra. ")
	print ("4.  Renombrar categoría.")
	print ("5.  Remover categoría.")
	print ("6.  Mostrar el contenido del archivo.")
	print ("7.  Crear datos de prueba (Borra existentes).")
	print ("8.  Reinicializar Archivo (Sin datos de prueba).")
	print ("9.  Ver configuración de teclas de interacción.")
	print ("10. Configurar teclas de interacción.")
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
		except Exception as ex:
			print(ex)

	elif i == 2:
		cat = input("Nombre de la categoría: ")
		name = input ("Ingrese el nombre que quiere modificar: ")
		rename = input ("Ingrese nuevo nombre: ")
		level = int (input ("Ingrese nivel: "))
		try:
			e.renameWord (cat, name, rename, level)
		except (Exception, KeyError, ValueError) as ex:
			print(ex)

	elif i == 3:
		cat = input("Ingrese categoría: ")
		name = input ("Ingrese nombre que desea eliminar: ")
		level = int (input ("Ingrese nivel: "))
		try:
			e.removeWord (cat, name, level)
		except (Exception, KeyError, ValueError) as ex:
			print(ex)

	elif i ==4:
		cat = input("Nombre de la categoría que desea modificar: ")
		newCat = input ("Nombre nuevo de la categoría: ")
		level = int (input ("Ingrese nivel: "))
		try:
			e.renameCategory (cat, newCat, level)
		except (Exception, KeyError) as ex:
			print(ex)

	elif i == 5:
		cat = input("Nombre de la categoría que desea eliminar: ")
		level = int (input ("Ingrese nivel: "))
		try:
			e.removeCategory (cat, level)
		except (Exception, KeyError) as ex:
			print(ex)

	elif i == 6:
		pp = pprint.PrettyPrinter(depth=7)
		pp.pprint(e.showFullData())

	elif i == 7:
		print("###########################################\n")
		print("Tener en cuenta que estos datos son puramente de prueba, por lo que no existen validaciones.\nSi desea datos validados, deber agregar de una palabra por vez (Opción 1)\nEl fin de esta opción es demostrar el funcionamiento del juego.")
		print("\n###########################################")
		e.testData()

	elif i == 8:
		e.reinitialize()

	elif i == 9:
		pp = pprint.PrettyPrinter(depth=2)
		pp.pprint(e.getTeclas())

	elif i == 10:
		dic    = e.getTeclas()
		keys   = dic.keys()

		DICTIONARY = {
			"FLECHA_IZQ": 143,
			"FLECHA_DER": 145,
			"FLECHA_ARR": 146,
			"FLECHA_ABA": 144,
			"F1" 		: 162,
			"F2"		: 163
		}

		
		print("############## Valores por defecto #################:\n")
		for k in keys:
			print(k + ": " + chr(dic[k]) + "\n")
		print("############## ################### #################:\n")	

		for k in keys:
			print("Para teclas especiales: ")
			for t in DICTIONARY.keys():
				print("'"+t+"' ( Entre comillas )")

			c = input("Ingrese la configuración para la tecla '" + k + "': ")
			if c.upper() == 'FLECHA_IZQ':
				c = DICTIONARY['FLECHA_IZQ']
			elif c.upper() == 'FLECHA_DER':
				c = DICTIONARY ['FLECHA_DER']
			elif c.upper() == 'FLECHA_ARR':
				c = DICTIONARY ['FLECHA_ARR']
			elif c.upper() == 'FLECHA_ABA':
				c = DICTIONARY ['FLECHA_ABA']
			elif c.upper () == 'F1':
				c = DICTIONARY ['F1']
			elif c.upper () == 'F2':
				c = DICTIONARY ['F2']
			if isinstance(c, str):
				try:
					c = ord(c)
					dic[k] = c
				except TypeError:
					print('Entrada no válida.')
					exit()
			else:
				dic[k] = c
		e.setTeclas(dic)

	elif i == 0:
		pass
	else:
		print("La opción ingresada no es válida")

exit()
