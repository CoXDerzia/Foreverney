class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")

data1 = input().split()
name1 = data1[0]
hp1 = int(data1[1])
dmg1 = int(data1[2])

m1 = Monster(name=name1, hp=hp1, dmg=dmg1)

data2 = input().split()
name2 = data2[0]
hp2 = int(data2[1])
dmg2 = int(data2[2])

m2 = Monster(name=name2, hp=hp2, dmg=dmg2)

while True:
    m2.hp -= m1.dmg
    if m2.hp < 0:
        m2.hp = 0
        break
    print(f'{m1.name} наносит удар')
    print(f'у {m2.name} осталось {m2.hp} HP')
    m1.hp -= m2.dmg
    if m1.hp < 0:
        m1.hp = 0
        break
    print(f'{m2.name} наносит удар')
    print(f'у {m1.name} осталось {m1.hp} HP')

if m1.hp > m2.hp:
    print(f'{m1.name} победитель')
elif m2.hp > m1.hp:
    print(f'{m2.name} победитель')
else:
    print("Ничья")