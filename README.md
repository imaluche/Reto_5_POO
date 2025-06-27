# Reto_5_POO
----------------------------------

### 1. paquete de shape como un modulo unico:
- Dentro de la carpeta 5_1 creamos el archivo principal (main.py) y una subcarpeta en la que se encontrar el __init__.py junto con el modulo shape (shape_1.py), el main importara de este archivo para usar las clases definidas.
### 2. Modulos individuales que importan de shape y heredan de el
- De manera similar al caso anterior dentro de la carpeta 5_2 definimos el archivo principal y el paquete shape
- dentro se encontaran 3 modulos junto con el __init__ (shape_1, rectangles, Triangles)
- Tanto el modulo rectangles como triangles importan de shape_1 (donde se define la clase base) y a partir de este declaran las clases de sus respectivas figuras, todas estas seran importadas por el archivo principal para ser usadas dentro de este.
