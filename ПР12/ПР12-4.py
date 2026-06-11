print("Программа считает количество 5 и 2")

marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
five = 0
two = 0

for mark in marks:
    if mark == 5:
        five += 1
    elif mark == 2:
        two += 1

print("Количество пятерок:", five)
print("Количество двоек:", two)