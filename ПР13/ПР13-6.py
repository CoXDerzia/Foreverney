numb = [8, 9, 10, 11]
print("Изначальное число: ", numb)

numb[1] = 17
numb.extend([4, 5, 6])
del numb[0]
numb.extend(numb.copy())
numb.insert(3, 25)
print("Измененное число: ", numb)