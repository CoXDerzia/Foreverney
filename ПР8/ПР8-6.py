print("Программа зашадывает случайное число и ваша задача угадать правильное число")

import random

passw = random.randint(1, 10)
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input("Напишите число от 1 до 10:"))
    attempts += 1

    if guess == passw:
        print("Вы угадали правильное число!")
        break
    elif attempts == max_attempts:
        print(f"Вы потратили все попытки. Верное число было {passw}.")
        break
    else:
        if guess > passw:
            print(f"Неверно. Загаднное число меньше вашего. Это была {attempts} попытка.")
        else:
            print(f"Неверно. Загаднное число больше вашего. Это была {attempts} попытка.")