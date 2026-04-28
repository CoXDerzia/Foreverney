n = int(input("Введите число, факториал которого хотите узнать:"))
factorial = 1

for i in range(1,n+1):
    factorial = factorial * i
print(f"Факториал числа {n} равен {factorial}")