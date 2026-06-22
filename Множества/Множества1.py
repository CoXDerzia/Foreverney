group1 = set(["Иван", "Мария", "Петр", "Сергей", "Анна"])
group2 = set(["Мария", "Анна", "Дмитрий", "Елена", "Сергей"])
print("Все студенты первой группы: ", end="")
print(*group1, sep=", ")
print("Все студенты второй группы: ", end="")
print(*group2, sep=", ")

people_in_all_groups = group1.intersection(group2)
print("Все студенты, которые ходят сразу в обе группы: ", end="")
print(*people_in_all_groups, sep=", ")

people_group1 = group1.difference(group2)
print("Все студенты,которые ходят только в первую группу: ", end="")
print(*people_group1, sep=", ")

people_group2 = group2.difference(group1)
print("Все студенты,которые ходят только во вторую группу: ", end="")
print(*people_group2, sep=", ")

all_people = group1.union(group2)
print("Все студенты, которые ходят хотя-бы в одну группу: ", end="")
print(*all_people, sep=", ")

people_only_one_group = group1.symmetric_difference(group2)
print("Все студенты, которые ходят только в одну группу: ", end="")
print(*people_only_one_group, sep=", ")
