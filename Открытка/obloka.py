import turtle


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

# =====================================================
# ПАРА 2 — ОБЛАКО
# =====================================================
def create_guest(x,y,color,size):
    guest = turtle.Turtle()
    guest.goto(x, y)
    guest.shape("circle")
    guest.pensize(5)
    guest.pendown()
    guest.shapesize(size)
    guest.color(color)
    guest.left(90)
    guest.forward(200)
    guest.penup()


create_guest(1, 1, "red", 1)

turtle.done()