Entrega.py
=============

Script para la generación de datos del juego


- Operaciones -
-------------------------------

e = Entrega()
	- Constructor

- e.addWord(word, category, level)
	- Almacena una palabra y su descripción de ayuda en una categoría de un determinado nivel (1..5).
	- Si la categoría no existe en ese nivel, la crea.
	- Una excepción ocurre si level no se encuentra en el rango.

- e.updateWord(wordOld, word, category, level)
	- Actualiza una palabra y su descripción de ayuda en una categoría de un determinado nivel (1..5).
	- Una excepción ocurre si la categoría ó la palabra a actualizar no existe ó bien el nivel no se encuentra en el rango.

- e.removeWord(word,category,level)
	- Remueve una palabra junto a su descripción de una categoría en un determinado nivel (1..5).
	- Una excepción occure, si la categoría no existe dentro del nivel, o bien el nivel no se encuentra en el rango.

- e.showFullData()
	- Muestra el estado actual de los datos dentro del archivo.

- e.renameCategory(categoryOld, category, level)
	- Renombra una categoría en un determinado nivel (1..5)
	- Una excepción ocurre si la categoría a reemplazar no existe o bien el nivel está fuera del rango.

- e.removeCategory(category, level)
	- Remueve una categoría junto a su información asociada de un determinado nivel (1..5)
	- Una excepción ocurre si la categoría no existe en el nivel, o bien el nivel se encuentra fuera del rango.
