print("Программа выводит, сколько людей стоят в очереди между Александрой и Левоном.")

count_between = 0
found_alexandra = False

while True:
    name = input("Введите имя участника: ")
    if name == "Александра":
        found_alexandra = True
        continue
    if name == "Левон":
        break
    if found_alexandra:
        count_between += 1
print("Людей между Александрой и Левоном: ", count_between)