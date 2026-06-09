print("Программа запрашивает ввод 4-х значного пин-кода")

password = 4590

while True:
    word= int(input("Введите пин-код:"))
    if word == 4590:
        print("Доступ разрешен")
        break
    if word != 4590:
        print("Ошибка. попробуйте еще раз")