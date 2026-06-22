log1 = set(input("Ввод 1: ").split())
log2 = set(input("Ввод 2: ").split())
log3 = set(input("Ввод 3: ").split())

in_all = log1.intersection(log2.intersection(log3))
all_ips = log1.union(log2.union(log3))
result = all_ips.difference(in_all)

print("Вывод: ", *sorted(result))