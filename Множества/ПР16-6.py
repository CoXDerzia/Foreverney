log1 = set(input("Ввод 1: ").split())
log2 = set(input("Ввод 2: ").split())
log3 = set(input("Ввод 3: ").split())

all_possible = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
all_ids = log1.union(log2.union(log3))
ghosts = []

for id in all_possible:
    if id not in all_ids:
        ghosts.append(id)
print("Вывод: ", *sorted(ghosts))