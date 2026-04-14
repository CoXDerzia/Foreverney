import random
x1 = random.randint(1,8)
y1 = random.randint(1,8)
x2 = random.randint(1,8)
y2 = random.randint(1,8)
kletka1 = (x1+y1)%2
kletka2 = (x2+y2)%2
if kletka1 == kletka2:
    print("YES")
else:
    print("NO")
print(kletka1, kletka2))
