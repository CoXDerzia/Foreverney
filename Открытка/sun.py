import turtle
def write_text():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-50, 45)
    t.color("purple")
    t.write("С 8 Марта!")
    t.goto(-50, 15)
    t.color("pink")
    t.write("Дорогие женщины!")
    t.goto(-50, -10)
    t.color("blue")
    t.write("Пусть каждый день будет ярким!")

    write_text()
    turtle.done()