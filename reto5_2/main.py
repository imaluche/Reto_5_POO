from shape.shape_1 import *
from shape.Rectangles import*
from shape.Triangles import*
if __name__ == "__main__":
    p0= Point(0, 0)
    p1= Point(0, 4)
    p2= Point(-3, 0)
    l0= Line(p0, p1)
    l1= Line(p1, p2)
    l3 = Line(p2,p0)
    l : list = [l0, l1, l3]
    escal= Trirectangle(l)
    print(f"el perimetro es: {escal.compute_perimeter()}")
    print(f"el area es: {escal.compute_area()}")
    print(f"los angulos internos son: {escal._inner_angles}")
    print(f"vertices:")
    for i in escal._vertices:
        print(f"({i.x},{i.y})")