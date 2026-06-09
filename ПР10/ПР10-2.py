print("Программа запрашивает ввод 3-х чисел по очереди,каждое больше предыдущего")

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

while True:
    if second <= first:
        while True:
            print("Ошибка. второе число должно быть больше первого")
            second = int(input("Введите второе число: "))
            if second > first:
                break
    third = int(input("Введите третие число: "))
    if third <= second:
        while True:
            print("Ошибка. третие число должно быть больше второго")
            third = int(input("Введите третие число: "))
            if third > second:
                break
    else:
        print(f"Последовательность {first}, {second}, {third} принята")
        break