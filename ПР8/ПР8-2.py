print("Программа считывает последовательность из 10 целых чисел и определяет, является ли каждое из них чётным.")
pruff = 0

for i in range(1, 11):
    num=int(input(f"{i}: "))
    if num %2 == 0:
        pruff +=1

if pruff == 10:
        print("YES")
else:
        print("NO")
