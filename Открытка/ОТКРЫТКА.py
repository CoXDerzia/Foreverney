import turtle

COLOR_CLOUD = "white"

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)


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
t.goto(280, 190)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(60)
t.end_fill()

t.color("green")
for i in range(30):
    t.penup()
    t.goto(-300 + i * 25, -300)
    t.pendown()
    d = 1 if i % 2 == 0 else -1
    t.setheading(90 + (i % 5) * 10)
    t.width(3 - (i % 2))
    n = 70 + (i % 30)
    for j in range(int(n / 10)):
        t.forward(10)
        t.left(14 * d)
    t.width(1)

def creat_player(x,y,color,size):
    player = turtle.Turtle()
    player.shape("circle")
    player.color(color)
    player.shapesize(size)
    player.penup()
    player.goto(x,y)
    player.stamp()
def create_guest(x,y,color,size):
    guest = turtle.Turtle()
    guest.penup()
    guest.goto(x, y)
    guest.shape("circle")
    guest.pensize(5)
    guest.pendown()
    guest.shapesize(size)
    guest.color(color)
    guest.left(90)
    guest.forward(200)
    guest.penup()



t.penup()
t.goto(0, 45)
t.pendown()
t.color("purple")
t.write("С 8 Марта!", align="center", font=("Arial", 36, "bold"))
t.penup()
t.goto(0, 15)
t.pendown()
t.color("deeppink")
t.write("Дорогие женщины!", align="center", font=("Arial", 20, "italic"))
t.penup()
t.goto(0, -10)
t.pendown()
t.color("blue")
t.write("Пусть каждый день будет ярким!", align="center", font=("Arial", 14, "normal"))



creat_player(100, 240, "white", 6)
creat_player(50, 230, "white", 5)
creat_player(-100, 240, "white", 6)
creat_player(-150, 230, "white", 5)
creat_player(-300, 240, "white", 6)
creat_player(-350, 230, "white", 5)

creat_player(-300, 50, "red", 4)
creat_player(-250, 50, "red", 4)
creat_player(-275, 22, "red", 5)
creat_player(300, 50, "red", 4)
creat_player(250, 50, "red", 4)
creat_player(275, 22, "red", 5)

create_guest(0, -300, "dark green", 1)
creat_player(0, -50, "pink", 4)
creat_player(0, -150, "pink", 4)
creat_player(50, -75, "pink", 4)
creat_player(50, -125, "pink", 4)
creat_player(-50, -75, "pink", 4)
creat_player(-50, -125, "pink", 4)
creat_player(0, -100, "yellow", 4)

create_guest(-200, -300, "dark green", 1)
creat_player(-200, -50, "red", 4)
creat_player(-200, -150, "red", 4)
creat_player(-150, -75, "red", 4)
creat_player(-150, -125, "red", 4)
creat_player(-250, -75, "red", 4)
creat_player(-250, -125, "red", 4)
creat_player(-200, -100, "yellow", 4)

create_guest(200, -300, "dark green", 1)
creat_player(200, -50, "blue", 4)
creat_player(200, -150, "blue", 4)
creat_player(250, -75, "blue", 4)
creat_player(250, -125, "blue", 4)
creat_player(150, -75, "blue", 4)
creat_player(150, -125, "blue", 4)
creat_player(200, -100, "yellow", 4)

turtle.done()
