import random
x1 = random.randint(1,8)
y1 = random.randint(1,8)
x2 = random.randint(1,8)
y2 = random.randint(1,8)
print(x1, y1, x2, y2)
if (x1 == x2) or (y1 == y2) or (x1 - x2 == y1 - y2) or (x1 - x2 == -(y1 - y2)):
    print("YES")
elif (x1 != x2) and (y1 != y1) and (x1 - x2 != y1 - y2) and (x1 - x2 != -(y1 - y2)):
    print("NO")
else:
    print("NO")