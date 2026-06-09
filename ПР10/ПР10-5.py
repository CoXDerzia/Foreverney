print("упрощенное меню банкомата")

capital = 1000

while True:
    print(" ")
    print("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")
    action = int(input("Введите интересущую вам операцию: "))
    if action == 1:
        print(f"Ваш баланс составляет {capital} рублей")
    if action == 2:
            if capital > 100:
                capital -= 100
                print("Снято 100 рублей")
                continue
            elif capital < 100:
                print("Недостаточно средств")
                continue
    if action == 3:
        capital += 100
        print("На счет добавлено 100 рублей")
    if action == 4:
        break
