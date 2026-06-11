numb=int(input("Введите число: "))

while numb>=10:
    sum=0
    while numb > 0:
        sum += numb%10
        numb//=10
        print(sum, end=" ")
        print(numb, end=" ")
    numb=sum

print(numb)