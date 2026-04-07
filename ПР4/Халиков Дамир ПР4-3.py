print("Задание 3")
numb=int(input("введите четырехзначное число: "))

ths= numb//1000
hnd= (numb//100) %10
tns= (numb//10) %10
nts= numb %10

print("Цифра в позиции тысяч = ", ths)
print("Цифра в позиции сотен = ", hnd)
print("Цифра в позиции десятков = ", tns)
print("Цифра в позиции единиц = ", nts)