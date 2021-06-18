import turtle
import random
import copy


screen = turtle.Screen()
turtle.setup(1024, 720)
turtle.bgpic("wallpaper.png")
turtle.title("Conway's Game of Life")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)

""" Living cells """
life_turtle = turtle.Turtle()  # turtle for drawing life
life_turtle.up()
life_turtle.hideturtle()
life_turtle.speed(0)

n = 50  # nxn grid


""" ------------------------ Creating lives ------------------------ """

life = list()  # create an empty list


def init_lives():
    for i in range(n):
        life_row = []  # a row of lives
        for j in range(n):
            if random.randint(0, 3) == 0:  # 1/3 probability of life
                life_row.append(1)  # 1 means life
            else:
                life_row.append(0)  # 0 means no life
        life.append(life_row)  # add a row to the life list -> life is a list of list


""" ------------------------ Printing life ------------------------ """


def draw_square(x, y, size):  # draws a filled square
    colors = ["#4A235A", "#4A235A", "#4A235A", "#FF00FF"]
    life_turtle.up()
    life_turtle.goto(x, y)
    life_turtle.down()
    life_turtle.seth(0)
    life_turtle.begin_fill()
    for i in range(4):
        life_turtle.color(colors[i])
        life_turtle.fd(size)
        life_turtle.left(90)
    life_turtle.end_fill()


def draw_life(x, y):  # draws life in (x,y)
    lx = 600/n*x - 300  # converts x,y to screen coordinate
    ly = 600/n*y - 300
    draw_square(lx + 1, ly + 1, 600 / n - 2)


def draw_all_life():  # draws all life
    global life
    for i in range(n):
        for j in range(n):
            if life[i][j] == 1:
                draw_life(i, j)  # draw live cells


""" ------------------------ Life cycle ------------------------ """


def num_neighbors(x, y):  # computes the number of life neighbours for cell[x,y]
    sum = 0
    for i in range(max(x - 1, 0), min(x + 1, n - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, n - 1) + 1):
            sum += life[i][j]
    return sum - life[x][y]


def update_life():  # update life for each cycle
    global life
    new_life = copy.deepcopy(life)  # make a copy of life
    for i in range(n):
        for j in range(n):
            k = num_neighbors(i, j)
            if k < 2 or k > 3:
                new_life[i][j] = 0
            elif k == 3:
                new_life[i][j] = 1
    life = copy.deepcopy(new_life)  # copy back to life
    life_turtle.clear()  # clears life in previous cycle
    draw_all_life()
    screen.update()
    screen.ontimer(update_life, 100)  # update life every 0.1 second


init_lives()
update_life()
turtle.done()
