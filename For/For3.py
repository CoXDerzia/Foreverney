m = int(input("Введите большее число:"))
n = int(input("Введите меньшее число:"))
if m>n:
    for i in range(n, m+1):
        print(i)
else:
    for i in range(n, m-1, -1):
        print(i)