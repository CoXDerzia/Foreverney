print("Программа получает число и ищет его индекс")

numbers = [10, 20, 30, 40, 50]
search_numb = int(input("Введите число для поиска: "))
found = False

for i in range(len(numbers)):
    if search_numb == numbers[i]:
        print(f"Индекс числа {search_numb} равен {i}")
        found = True
        break
if found == False:
    print("Такого числа нету в списке")