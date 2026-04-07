import math

def tochki(x1,y1,x2,y2):
    xy = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return xy

x1, y1= map(float, input("Введите координаты первой точки(x y): ").split())
x2, y2= map(float, input("Введите координаты второй точки(x y): ").split())
print(f"Евклидово расстояние между двумя точками = {tochki(x1, y1, x2, y2):.2f} математических единиц")