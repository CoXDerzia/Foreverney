m = int(input("Введите первое число:"))
n = int(input("Введите второе число:"))
for i in range(m,n+1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)