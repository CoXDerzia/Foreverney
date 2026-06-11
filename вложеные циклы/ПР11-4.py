print("Программа запрашивает натуральное число и далее вычесляет значения для каждого вопроса")

num = int(input("Напишите натуральное число: "))
numb=num
#Программа должна делять число и считать каждую цифру выполняя требованиям
sum3 = 0
last = numb % 10
count_last = 0
even = 0
sum_bolee5 = 0
mult_bolee7 = 1
or0or5 = 0
while numb > 0:
    digit=numb % 10
    if digit == 3:
        sum3 += 1
    if digit == last:
        count_last += 1
    if digit % 2 == 0:
        even += 1
    if digit > 5:
        sum_bolee5 += digit
    if digit > 7:
        mult_bolee7 *= digit
    if digit == 5 or digit == 0:
        or0or5 += 1
    numb //= 10
print(f"В числе {num} всего {sum3} троек")
print(f"В числе {num} цифра {last} встречается {count_last} раз")
print(f"В числе {num} четные числа встречаются {even} раз")
print(f"В числе {num} сумма цифр больше 5 составляет {sum_bolee5}")
if mult_bolee7 == 1:
    print(f"В числе {num} нету цифр более 7 {mult_bolee7}")
else:
    print(f"В числе {num} произведение цифр больше 7 составляет {mult_bolee7}")
print(f"В числе {num} 0 и 5 встречаются {or0or5} раз")
