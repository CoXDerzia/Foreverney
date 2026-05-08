n = int(input("Введите натуральное число: "))
sum=0
for i in range(1, n+1):
    if(i % 2 == 0):
        sum = sum - i
    else:
        sum = sum + i
print(f"1-2+3-4+5-6+...+(-1)^{n}+1 * {n} = {sum}")