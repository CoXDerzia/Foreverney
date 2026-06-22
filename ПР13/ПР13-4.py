ip = input("Введите ip-адрес: ")
address = ip.split(".")
if address != 4:
    print("НЕТ")
    exit()
for i in range(len(address)):
    address[i] = int(address[i])
    if address > 255 or address < 0:
        print("НЕТ")
        exit()
    else:
        print("ДА")