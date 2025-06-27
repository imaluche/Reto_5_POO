# Reto_5_POO
----------------------------------

### 1. paquete de shape como un modulo unico:
- Dentro de la carpeta 5_1 creamos el archivo principal (main.py) y una subcarpeta en la que se encontrar el modulo shape (shape_1.py) junto con el __init__.py, el main importara de este unico archivo para usar las clases definidas.
### 2. Modulos individuales que importan de shape y heredan de el
- De manera similar al caso anterior dentro de la carpeta 5.2 definimos el archivo principal y el paquete shape, en este caso dentro se encontaran 3 modulos junto con el __init__ (shape_1, rectangles, Triangles)
- Tanto el modulo rectangles como triangles importan de shape_1 y a partir de este declaran las clases de sus respectivas figuras, todas estas seran importadas por el archivo principal para ser usadas dentro de este.
