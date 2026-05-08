print("Программа загадывает случайное число и ваша задача угадать правильное число")

import random

passw = random.randint(1, 10)

for attempt in range(1, 4):
    guess = int(input("Напишите число от 1 до 10:"))
    if guess == passw:
        print("Вы угадали правильное число!")
        break
    elif guess > passw:
        print(f"Неверно. Загаднное число меньше вашего.")
    else:
        print(f"Неверно. Загаднное число больше вашего.")
else:
    print(f"Вы потратили все попытки. Верное число было {passw}.")
