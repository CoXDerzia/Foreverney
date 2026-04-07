print("Задание 6")
import math

x_gr=int(input("Введите угол в градусах: "))

x_rdn=math.radians(x_gr)
trg=math.sin(x_rdn)+math.cos(x_rdn)+math.tan(x_rdn)**2

print(trg)