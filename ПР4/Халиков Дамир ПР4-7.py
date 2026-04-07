print("Задание 7")
SEATS_PER_COMPARTMENT = 4
seat_numb= int(input("Введите номер места:"))
cupe_numb = (seat_numb-1) // SEATS_PER_COMPARTMENT+1
print("Ваше", seat_numb, "место находится в купе", cupe_numb)