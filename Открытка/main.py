import turtle

COLOR_CLOUD = "white"

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

# =====================================================

t.color("white")
coords = [
    (100, 280, 40),
    (70, 290, 30),
    (130, 290, 30),
    (50, 270, 25),
    (150, 270, 25),
    (100, 260, 35)
]
for a, b, r in coords:
    t.penup()
    t.goto(a, b - r)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

turtle.done()
#сердца
t.penup()
t.goto(-300, 50)
t.pendown()
t.color("red")
t.begin_fill()
t.setheading(140)
t.forward(62)
t.circle(-35, 200)
t.setheading(60)
t.circle(-35, 200)
t.forward(62)
t.end_fill()

# НАДПИСЬ
t.penup()
t.goto(0, 15)
t.pendown()
t.color("purple")
t.write("С 8 Марта!", align="center", font=("Arial", 36, "bold"))
t.penup()
t.goto(0, 15)
t.pendown()
t.color("deeppink")
t.write("Дорогие женщины!", align="center", font=("Arial", 20, "italic"))
t.penup()
t.goto(0, 10)
t.pendown()
t.color("blue")
t.write("Пусть каждый день будет ярким!", align="center", font=("Arial", 14, "normal"))
#цветки
t.color("darkgreen")
t.width(4)
t.penup()
t.goto(0, -300)
t.pendown()
t.setheading(90)
t.forward(120)
t.width(1)
t.color("pink")
for i in range(8):
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.setheading(i * 45)
    t.begin_fill()
    t.circle(30, 180)
    t.circle(30, 180)
    t.end_fill()
t.penup()
t.goto(0, -180)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(20)
t.end_fill()

#трава
t.color("green")
for i in range(12):
    t.penup()
    t.goto(-300 + i * 25, -300)
    t.pendown()
    d = 1 if i % 2 == 0 else -1
    t.setheading(75 + (i % 5) * 10)
    t.width(3 - (i % 2))
    n = 70 + (i % 30)
    for j in range(int(n / 10)):
        t.forward(10)
        t.left(5 * d)
    t.width(1)
#солнце
t.color("orange")
t.width(6)
for i in range(16):
    t.penup()
    t.goto(300, 250)
    t.pendown()
    t.setheading(i * 22.5)
    t.forward(90)
t.width(1)
t.penup()
t.goto(350, 190)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(60)
t.end_fill()

turtle.done()

def creat_player(x,y,color,size):
    player = turtle.Turtle()
    player.shape("Turtle")
    player.color(color)
    player.shapesize(size)
    player.penup()
    player.goto(x,y)

creat_player(100, 280 - 40, COLOR_CLOUD, 4)