ip = input("Введите ip-адрес: ")
address = ip.split(".")
if len(address) != 4:
    print("НЕТ")
    exit()
else:
    valid_ip = True
    for ip in address:
        if 0 <= int(ip) <= 255:
            valid_ip = False
if valid_ip == True:
    print("ДА")
else:
    print("НЕТ")
#Неправильно