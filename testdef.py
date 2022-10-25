
import turtle as t
import math


def draw_house(walls_x, walls_y):
    """
    walls_x - левый нижний угол стены
    walls_y - правый нижний угол стены
    walls_width - ширана стен
    walls_heigh - высота стен
    door_x
    door_y
    door_width
    door_heigt
    """


    door_x = door_width + walls_width / 2 - door_width / 2
    door_y = walls_x


    draw_walls(x, y, walls_width, walls_height, )
    draw_door()
    draw_roof()



def draw_walls():
    print(f"стены рисуют {walls_x}, {walls_y}")
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fillcolor
    t.begin
def draw_door():
    print("нарисовали дверь")

def draw_roof():
    print("нарисовали крышу")

draw_house(-100, -200, 350, 200, 70, 90 )


t.done()