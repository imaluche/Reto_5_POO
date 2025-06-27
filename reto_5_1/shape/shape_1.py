from math import acos, degrees
class Point: #definimos el punto por dos coordenadas en el plano
  def __init__(self, x: float, y: float): 
    self.x = x
    self.y = y
  def redo(self,nx,ny):
    self.x = nx
    self.y = ny
class Line:
   def __init__(self, ps:Point, pe:Point): #definimos un segmento de recta con 2 puntos
      self.start = ps
      self.end = pe
      if (self.start.y == self.end.y):
         q ="recta horizontal"
      elif (self.start.x == self.end.x):
         q ="recta vertical"
      else:
         q = (self.start.y - self.end.y)/(self.start.x - self.end.x)
      self.slope= q #definimos la pendiente de la recta a la cual pertenece el segmento
   def lenght(self):
      return float(((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5) 
   def function(self,x:float)->float:
      if self.slope == "recta horizontal":
         if self.start.y == 0:
            return "horizontal en el origen"
         else: 
            return "horizontal fuera del origen"
      if self.slope == "recta vertical":
         if self.start.x == 0:
            return "vertical en el origen"
         else: 
            return "vertical fuera del origen"
      b= self.start.y - ((self.slope)*(self.start.x))
      f=self.slope*x + b #definimos los componentes para formar la ecuacion de la recta
      return f
   def vertical_cross(self):
      if self.function(self.start.x) == "vertical en el origen":
            print("interseca con el eje y en toda su longitud ")
      elif self.function(self.start.x) == "vertical fuera del origen":
          print( "la recta vertical no interseca con el eje y")
      else:
         for i in range (self.start.x, self.end.x):
            if self.function(i) == self.function(0):
             print("interseca con y en: ")
             return i
            else:
               print("no interseca con y")
   def horizontal_cross(self):
      if self.function(self.start.y) == "horizontal en el origen":
            print("interseca con el eje x en toda su longitud ")
      elif self.function(self.start.y) == "horizontal fuera del origen":
          print( "la recta horizontal no interseca con el eje x")
      else:
         n=False
         for i in range (self.start.y, self.end.y):
            if i==0:
               n=True
               f=i
         if n==True:
            print("interseca con x en: ")
            return f
         else:
            print("no interseca con x")
   def discretizador(self,n):
      i:float=self.start.x
      l:list=[]
      while i<=self.end.x:
         if self.slope == "recta horizontal":
            l.append(Point(i,self.function(i)))
         elif self.slope == "recta vertical":
            l.append(Point(self.start.x,i))
         else:
            l.append(Point(i, self.function(i)))
         i= i + n  
      return l    
class Shape: #creamos la clase base con los metodos mas generales
    def __init__(self,aristas:list):
        self.is_regular = False
        self._aristas = aristas
        self._vertices = []
        self._inner_angles = [] 
    def compute_perimeter(self): 
        return None
    def compute_area(self):
        return None
    def get_aristas(self):
        pass
    def get_vertices(self):
        pass
    def get_inner_angles(self):
        pass
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
class Triangle(Shape):#hereda de shape
    def __init__(self, aristas: list):
        if len(aristas) != 3:
            raise ValueError("Un triangulo debe tener 3 lados coincidentes") #al menos se ncesitan 3 lineas
        else:
            super().__init__(aristas)
            self._lado1= aristas[0]
            self._lado2= aristas[1]
            self._lado3= aristas[2]
            self.is_regular = False
            self._aristas = aristas
            self._vertices = [aristas[0].start, aristas[1].start, aristas[2].start] #los vertices son 3 puntos que son inicios/finales de las lineas
            inner = []
            for i in aristas: #recorre todos los lados para formar todos los angulos internos
                b= 1
                c= 2
                if i == aristas[1]:
                    b= 0
                    c= 2
                if i == aristas[2]:
                    b= 0
                    c= 1 
                va= i.lenght()
                vb= self._aristas[b].lenght()
                vc= self._aristas[c].lenght()               
                teocos = (((va)**2)-((vb)**2)-((vc)**2))/(-2*(vb*vc)) #teorema del coseno
                ang = acos(teocos)
                inner.append(degrees(ang)) #añadimos el angulo
            self._inner_angles = inner
    def compute_perimeter(self):
        return self._lado1.lenght() + self._lado2.lenght() + self._lado3.lenght()
    def compute_area(self):
        s = self.compute_perimeter() / 2
        a = self._lado1.lenght()
        b = self._lado2.lenght()
        c = self._lado3.lenght()
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 #formula de heron (no es necesaria la altura ni base)
        return area
    def get_aristas(self):
        return self._aristas
    def get_vertices(self):
        return self._vertices
    def get_inner_angles(self):
        return self._inner_angles
class Equilatero(Triangle): #caso especifico de triangulo, todos sus lados son iguales
    def __init__(self, lado:Line): #solo se necesita un lado
        if (lado.slope == "recta vertical" or lado.slope == "recta horizontal"):
            raise ValueError("Un triangulo equilatero debe tener 3 lados coincidentes y no ser rectos")
        else:
            lado2 = Line(lado.end, Point(2*(lado.end.x), lado.start.y))
            lado3= Line(lado.start, lado2.end)
            #construimos los demas lados a partir del original
            super().__init__([lado,lado2,lado3]) 
            self.is_regular = True #el unico triangulo regular
            self.__aristas = [lado, lado2, lado3]
            self.__vertices = [lado.start, lado.end, lado2.end]
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles
class Isoceles(Triangle): #caso especifico, dos de sus lados son iguales
    def __init__(self, ladodoble:Line): #solo ingresamos una linea
        if ladodoble.slope == "recta vertical" or ladodoble.slope == "recta horizontal":
            raise ValueError("Un triangulo isoceles debe tener 3 lados coincidentes")
        else:
            ladoespejo = Line(ladodoble.end, Point(2*(ladodoble.end.x), ladodoble.start.y)) #construimos el segundo lado igual, conociendo ambos podemos definir el tercero
            super().__init__([ladodoble, ladoespejo, Line(ladodoble.start, ladoespejo.end)])
            self.__aristas = [ladodoble, ladoespejo, Line(ladodoble.start, ladoespejo.end)]
            self.__vertices = [ladodoble.start, ladodoble.end, ladoespejo.end]
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles
    
class Escaleno(Triangle): #todos los lados diferentes
    def __init__(self, aristas: list):
        confirm :bool= aristas[0].lenght() != aristas[1].lenght != aristas[2].lenght()
        if len(aristas) != 3 or confirm == False:
            raise ValueError("Un triangulo escaleno debe tener 3 lados coincidentes y de diferente longitud")
        else:
            super().__init__(aristas)
            self.__aristas = self._aristas 
            self.__vertices = self._aristas
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles
class Trirectangle(Triangle): #hay un angulo de 90 grados
    def __init__(self, aristas: list):
        if len(aristas) != 3 or (aristas[0].slope == "recta vertical" and aristas[1].slope == "recta horziontal"): #dos lados siempre seran rectos por el angulo de 90
            raise ValueError("Un triangulo trirectangulo debe tener 3 lados coincidentes y uno de ellos debe ser vertical y otro horizontal")
        else:
            super().__init__(aristas) 
            self.__aristas = self._aristas
            self.__vertices = self._aristas
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles      