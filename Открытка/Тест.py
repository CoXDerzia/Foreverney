import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

def flower_draw(x,y,color,size):
    flower = turtle.Turtle()
    flower.shape("circle")
    flower.color(color)
    flower.shapesize(size)
    flower.penup()
    flower.goto(x, y)
    flower.stamp()