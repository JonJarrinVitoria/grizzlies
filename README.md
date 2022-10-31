# Grizzlies   Parseador de un archivo csv a json, y de un archivo json a csv.
# ¿Qué es Grizzlies?
Es una librería capaz de leer archivos tanto en formato csv como json, además de convertirlos a csv o json y guardarlos en un directorio especificado por el usuario.
# ¿Qué aporta la librería grizzlies?
* Ser capaz de leer archivos csv por el delimitador que se le indique.
* Detección automatica del tipo de archivo introducido.
* Dependiendo del tipo de archivo introducido, sabe a que lo debe convertir y como guardarlo.
* Sencilla utilización. El usuario solo debe poner llamar a la clase y al método que desea realizar. (ejem: gz.guardar(nombre del archivo))
# Código fuente y cómo instalarlo.
El repositorio github donde se encuentra el código fuente es el siguiente:
https://github.com/JonJarrinVitoria/Grizzlies.git
```
pip install grizzlies
```
# ¿Cómo funciona grizzlies?
## Ejemplo de configuración y utilización con un archivo csv:

El primer paso es importar la librería y configurarla.
```
 import grizzlies as gz
 gz = gz.grizzlies()
```
Procedemos a leer el arhivo csv. En este caso, al ser un arhivo csv, le debemos introducir el nombre del archivo y el delimitador en caso de ser diferente a ";".
```
  gz.leer('./MiDirectorio/archivo.csv', delimitador=';')
```
En el siguiente paso, convertiremos nuestro archivo csv a tipo json. En este caso, no hace falta introducir nada, ya que coge la información del paso anterior, y sabe identificar que tipo de archivo es, y por ende, a cual debe convertirlo:
```
  gz.convertir()
```
Finalmente, para poder guardar el arhivo, le indicaremos el directorio donde lo queremos guardar, el nombre con el que lo queremos que se guarde, junto con la extensión a la cual lo hemos convertido:
```
  gz.guardar('./MiDirectorio/archivo.json')
```
# Dependencias
* [flatten_json - poner que hace esta libreria]()
  - [pip install flatten_json](https://pypi.org/project/flatten-json/)
