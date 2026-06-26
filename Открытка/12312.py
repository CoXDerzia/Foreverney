import turtle


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)


def draw_flowers():
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.hideturtle()
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

def create_player(x, y, color, size):
    player = turtle.Turtle()
    player.shape("circle")
    player.color(color)
    player.shapesize(stretch_wid=size, stretch_len=size)
    player.penup()
    player.goto(x, y)
    player.stamp()
    player.hideturtle()


def create_guest(x, y, color, size):
    guest = turtle.Turtle()
    guest.penup()
    guest.goto(x, y)
    guest.shape("circle")
    guest.color(color)
    guest.shapesize(stretch_wid=size, stretch_len=size)
    guest.left(90)
    guest.pendown()
    guest.forward(200)
    guest.penup()
    guest.hideturtle()


def write_text():
    t = turtle.Turtle()
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


def draw_sun():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(300, 250)
    t.pendown()
    t.width(6)
    for i in range(16):
        t.setheading(i * 22.5)
        t.forward(90)
    t.width(1)


def draw_circle():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(280, 190)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

draw_flowers()
write_text()
draw_circle()

create_player(100, 240, "white", 6)
create_player(50, 230, "white", 5)
create_player(-100, 240, "white", 6)
create_player(-150, 230, "white", 5)
create_player(-300, 240, "white", 6)
create_player(-350, 230, "white", 5)
create_player(-300, 50, "red", 4)
create_player(-250, 50, "red", 4)
create_player(-275, 22, "red", 5)
create_player(300, 50, "red", 4)
create_player(250, 50, "red", 4)
create_player(275, 22, "red", 5)

create_guest(0, -300, "darkgreen", 1)
create_guest(-200, -300, "darkgreen", 1)
create_guest(200, -300, "darkgreen", 1)


create_player(0, -50, "pink", 3)
create_player(0, -150, "pink", 3)
create_player(50, -75, "pink", 3)
create_player(50, -125, "pink", 3)
create_player(-50, -75, "pink", 3)
create_player(-50, -125, "pink", 3)
create_player(0, -100, "yellow", 3)

create_player(-200, -50, "red", 3)
create_player(-200, -150, "red", 3)
create_player(-150, -75, "red", 3)
create_player(-150, -125, "red", 3)
create_player(-250, -75, "red", 3)
create_player(-250, -125, "red", 3)
create_player(-200, -100, "yellow", 3)

create_player(200, -50, "blue", 3)
create_player(200, -150, "blue", 3)
create_player(250, -75, "blue", 3)
create_player(250, -125, "blue", 3)
create_player(150, -75, "blue", 3)
create_player(150, -125, "blue", 3)
create_player(200, -100, "yellow", 3)

turtle.done()