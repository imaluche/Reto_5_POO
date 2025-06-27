from shape.shape_1 import Point, Line, Shape
class Rectangle(Shape): #hereda de shape
    def __init__(self, aristas:list):
        if len(aristas) != 2:
            raise ValueError("El rectangulo debe tener 4 vertices.") #se necesitan minimo 2 lineas para construir el rectangulo
        else:
            flag:bool = (aristas[0].slope == "recta vertical" and aristas[1].slope == "recta horizontal") and (aristas[0].end == aristas[1].start) #las lineas deben ser verticales u horziontales)
            if flag:
             super().__init__(aristas)
             self._aristas = self._aristas
             self.is_regular = True
             self.base = aristas[1]
             self.altura = aristas[0]
             self._vertices = [(aristas[0].start), aristas[0].end, aristas[1].end, Point((aristas[0].start.x) + (aristas[1].lenght()), aristas[0].start.y)] 
             self._inner_angles = [90, 90, 90, 90] #los angulos siempre son 90 grados
    def compute_perimeter(self):
        return 2 * (self.base.lenght() + self.altura.lenght())
    def compute_area(self):
        return self.base.lenght() * self.altura.lenght()
    def get_inner_angles(self):
        return self._inner_angles
    def get_aristas(self):
        return self._aristas
    def get_vertices(self):
        return self._vertices
class Square(Rectangle): #caso especifico del rectangulo
    def __init__(self, lado:Line):
        if len(lado) != 1:
            raise ValueError("Solo es necesario ingresar una linea recta para formar el cuadrado.") #solo se necesita una linea para formar un cuadrado
        else:
            flag:bool = lado[0].slope == "recta vertical" or lado.slope == "recta horizontal"
            if flag:
                ladob= Line(lado[0].end, Point(lado[0].end.x + lado[0].lenght(), lado[0].end.y))
                super().__init__([(lado[0]),ladob])
                self.__aristas = self._aristas
                self.__vertices = self._vertices
                self.__inner_angles = self._inner_angles
    def get_inner_angles(self):
        return self.__inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices