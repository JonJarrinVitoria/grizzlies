# Grizzlies   Parseador de un archivo csv a json, y de un archivo json a csv.
# ¿Que es Grizzlies? 
Es una libreria capaz de leer archivos tanto en formato csv como json, además de convertilos a csv o json y guardarlos en un directorio especificado por el usuario.
# ¿Que aporta la librería Grizzliers?
* Ser capaz de leer archivos csv por el delimitador que se le indique.
* Detección automatica del tipo de archivo introducido.
* Dependiendo del tipo de archivo introducido, sabe a que lo debe convertir y como guardarlo.
* Sencilla utilización. El usuario solo debe poner . y la acción que desea realizar.(ejem: gz.guardar(nombre del archivo))
# Codigo fuente y como instalarlo.
El repositorio github donde se encuentra el código fuente es el siguiente: 
https://github.com/JonJarrinVitoria/Grizzlies.git 
```
pip install grizzlies
```
# ¿Cómo funciona Grizzlies?
## Ejemplo de configuración y utilización con un archivo csv:
poner aqui una imagen de como es el csv.
El primer paso es importar la libreria y configurarla.
```
 import grizzlies as gz
 gz = gz()
```
Procedemos a leer el arhivo csv. En este caso, al ser un arhivo csv, le debemos introducir el nombre del archivo y el delimitador.
```
  gz.leer('./MiDirectorio/archivo.csv', delimitador=';')
```
En el siguiente paso, convertiremos nuestro archivo csv a tipo json. En este caso, no hace falta introducir nada, ya que coge la información del paso anterior, y sabe identificar que tipo de archivo es, y por ende, a cual debe convertirlo:
```
  gz.convertir()
```
Finalmente, para poder guardar el arhivo, le indicaremos el directorio donde lo queremos guardar, el nombre con el que lo queremos que se guarde y añadir la extensión a la cual lo hemos convertido:
```
  gz.guardar('./MiDirectorio/archivo.json')
```
# Dependencias
* [json - Ponder que hace esta libreria](https://docs.python.org/es/3/library/json.html).
  - [pip install json](https://pypi.org/project/jsonlib/)
* [csv - poner que hace esta libreria](https://docs.python.org/es/3/library/csv.html)
  - [pip install csv](https://pypi.org/project/python-csv/)
* [flatten_json - poner que hace esta libreria]()
  - [pip install flatten_json](https://pypi.org/project/flatten-json/)
