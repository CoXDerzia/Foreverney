price = int(input("Введите цену за услугу Ведьмака: "))
coins = [25, 10, 5, 1]
coin_count = 0
i = 0
while price > 0:
    if price >= coins[i]:
        price -= coins[i]
        coin_count += 1
    else:
        i += 1
print(coin_count)