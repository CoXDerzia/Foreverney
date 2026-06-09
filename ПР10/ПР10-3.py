print("Программа находит самое большое число из последовательности веденных чисел, число 0 - сигнал остановки")

max_numb = 0

while True:
    numb = int(input("Введите число: "))
    if numb > max_numb:
        max_numb = numb
    if numb == 0:
        break

print(max_numb)