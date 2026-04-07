print("Задание 2")
import math

x1, y1= map(float, input("Введите координаты первой точки(x y): ").split())
x2, y2= map(float, input("Введите координаты второй точки(x y): ").split())

xy=math.sqrt((x1-x2)**2+(y1-y2)**2)
print(f"Евклидово расстояние между двумя точками = {xy:.2f} математических единиц")