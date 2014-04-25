Entrega
=============

Se debe importar el paquete "entrega1" el módulo "entrega" ( "from entrega1 import entrega" )

Luego de la importación debe instanciarse la clase Entrega.

e = entrega.Entrega()

a partir de este momento se pueden acceder a los metodos del objeto mismo.

Ellas son:


- Operaciones con categorías -
-------------------------------

e.categories() # Retorna todas las categorías ordenadas alfabeticamente.

e.addCategory(name) # Agrega una nueva categoría de nombre name.

e.removeCategory(name) # Remueve una categoría de nombre name.

e.renameCategory(oldName,newName) # Renombra una categoría de nombre oldName por newName.


- Operaciones con palabras -
-------------------------------

e.words() # Retorna todas las palabras agrupadas por categorías. Tanto las categorías como las palabras se encuentran ordenandas alfabeticamente.

e.wordsByCategoryName(category) # Retorna todas las palabras de una categoría category.

e.wordByCategoryName(category) # Retorna una palabra aleatoria, de la categoría category.

e.addWord(category,word) # Agrega una palabra word, a una categoría category.

e.removeWord(category,word) # Remueve la palabra word, de una categoría category.

e.renameWord(category,oldWord,newWord) # Renombra una palabra oldWord por newWord de una categoría category.






