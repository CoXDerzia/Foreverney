n = int(input())
product = 1 #при вводе единичного числа программа ранее искала остаток самого себе
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
