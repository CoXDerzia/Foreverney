numbers = input("Введите числа через пробел: ")

nums = numbers.split()
count = 0

for i in range (len(nums)):
    for j in range (i+1, len(nums)):
        if nums[i] == nums[j]:
            count += 1
            
print("Всего пар: ", count)