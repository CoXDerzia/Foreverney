print("программа запрашивает цену товаров и суммирует их, при 0 программа останавливается")

basket = 0

while True:
    print(f"Общая цена товаров = {basket}")
    price = int(input("Введите цену товара: "))
    if price > 0:
        basket += price

    if price < 0:
        print("Ошибка цены")
        continue
    if price == 0:
        break

if basket > 1000:
    discount = basket * 0.1
    print("Вам скидка 10%")
    print(f"К оплате {basket-discount}")
else:
    print(f"К оплате {basket}")