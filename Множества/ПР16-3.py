#server_a = set("data.db image.png log.txt".split())
#server_b = set("image.png script.py data.db".split())
#print("Ввод(Сервер A): ", *server_a)
#print("Ввод(Сервер B): ", *server_b)

server_a = set(input("Ввод(Сервер A):").split())
server_b = set(input("Ввод(Сервер B):").split())
print("Вывод: ")

common = server_a.intersection(server_b)
print("Общие: ", *common)

lost = server_a.difference(server_b)
print("Потерянные: ", *lost)
