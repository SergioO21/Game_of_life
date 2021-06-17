import turtle

screen = turtle.Screen()
turtle.setup(1024, 720)
turtle.title("Conway's Game of Life")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)

n = 30  # nxn grid


def draw_line(x1, y1, x2, y2):  # this function draw a line between x1,y1 and x2,y2
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)


def draw_grid():  # this function draws nxn grid
    turtle.pencolor('#FFBFBF')
    turtle.pensize(3)
    x = -300
    for i in range(n + 1):
        draw_line(x, -300, x, 300)
        x += 600 / n
    y = -300
    for i in range(n + 1):
        draw_line(-300, y, 300, y)
        y += 600 / n


draw_grid()
screen.update()
turtle.done()