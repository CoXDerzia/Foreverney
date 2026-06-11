import random

print("Программа получает 5 случайных чисел и меняет первый элемент с последним")

numbers = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100) , random.randint(1, 100)]

print("Изначальный список: ", numbers)

min_index = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i

numbers[min_index], numbers[0] = numbers[0], numbers[min_index]


print("Список с измененными элементами: ", numbers)