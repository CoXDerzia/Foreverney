cell = int(input("Введите номер ячейки: "))
if cell == 0:
    print("Ваш цвет зеленый")
elif (1<= cell <=10) or (19<= cell <=28):
    print("Ваш цвет черный")
elif (11<= cell <= 18) or (29<= cell <= 36):
    print("Ваш цвет красный")
else:
    print("Ошибка, данных чисел нет на колесе")