numb = [10, 5, 17, 3, 8]
print("Изначальный список: ", numb)

print("Длина списка: ", len(numb))

last_numb = numb.pop()
numb.append(last_numb)
print("Последний элемент списка: ", last_numb)

print("Список в обратном порядке: ", numb[::-1])

if 5 in numb and 17 in numb:
    print("Yes")
else:
    print("No")

del numb[0]
del numb[-1]
print("Список без первого и последнего чисел: ", numb)