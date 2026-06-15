prices_str = "100 50 200 150 75 300"

print("Изначальная строка: ", prices_str)

prices = prices_str.split(" ")

for i in range(len(prices)):
    prices[i] = float(prices[i])

prices.sort()
max_price = prices.pop()
prices.append(max_price / 2)
prices.sort()
print("Список цен: ", prices)
print("Средняя цена: ", sum(prices)//len(prices))