print("Программа создает список из нечетных чисел от 1 до n и выводит его")

numb = int(input("Введите число больше или равное 1: "))
while True:
    if numb >= 1:
        num = list(range(1,numb+1, 2))
        print(*num, sep=",")
        break
    else:
        print("Неправильный ввод данных, попробуйте еще раз")