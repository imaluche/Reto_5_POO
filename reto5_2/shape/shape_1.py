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

