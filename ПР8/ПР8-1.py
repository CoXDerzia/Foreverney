n=int(input("Введите число, на которое хотите узнать таблицу умножения: "))
for i in range(1, 11):
    multiplication = n*i
    print(f"{n}*{i} = {multiplication}")