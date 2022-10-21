import turtle as t
import math


def draw_house(walls_x, walls_y):
    """

    x - левый нижний угол стены
    y - правый нижний угол стены
    walls_width - ширана стен
    walls_heigh - высота стен
    """
    draw_walls(x, y, walls_width, walls_height, walls_color)
    draw_door()
    draw_roof()



def draw_walls():
    print(f"стены рисуют {walls_x}, {walls_y}")
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fill
def draw_door()
    print("нарисовали дверь")

def draw_roof():
    print("нарисовали крышу")

draw_house(-100, -200, 350, 200)


t.done()