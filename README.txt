Entrega
=============

Se debe importar el paquete "entrega1" el módulo "entrega" ( "from entrega1 import entrega" )

Luego de la importación debe instanciarse la clase Entrega.

e = entrega.Entrega()

a partir de este momento se pueden acceder a los metodos del objeto mismo.

Ellas son:


- Operaciones con categorías -
-------------------------------

e.categories() # Retorna todas las categorias ordenadas alfabeticamente

e.addCategory(name) # Agrega una nueva categoria de nombre name.

e.removeCategory(name) # Remueve una categoria de nombre name.

e.renameCategory(oldName,newName) # Renombra una categoria de nombre oldName por newName.


- Operaciones con palabras -
-------------------------------

e.words() # Retorna todas las palabras agrupadas por categorias. Tanto las categorias como las palabras se encuentran ordenandas alfabeticamente

e.wordsByCategoryName(category) # Retorna todas las palabras de una categoria

e.wordByCategoryName(category) # Retorna una palabra aleatoria, de la categoria category.

e.addWord(category,word) # Agrega una palabra word, a una category category

e.removeWord(category,word) # Remueve la palabra word, de una category category

e.renameWord(category,oldWord,newWord) # Renombra una palabra oldWord por newWord de una categoria category






