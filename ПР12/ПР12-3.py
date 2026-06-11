print("Программа изменяет список аккаунтов")

users = ["Admin", "Guest", "User", "Bot"]

print("Изначальный список аккаунтов: ", users)

users [2] = "Moderator"
users [-1] = "SuperAdmin"
users = users + ["Newbie"]

print("Измененный список аккаунтов: " ,users)