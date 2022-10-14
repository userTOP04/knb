import turtle as t
import math

t.shape("turtle")



walls_width = int(input("Ширина стен"))
walls_height = int(input("Высота стен "))
walls_color = input("Цвет стeн (heh) ")
roof_height = int(input("Высота крыши"))
roof_color = input("Цвет крыши (heh) ")
roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))


t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
    t.fd(walls_width)
    t.right(90)
    t.fd(walls_height)
    t.right(90)
t.end_fill()


t.fillcolor(roof_color)
t.begin_fill()
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180)
t.fd(roof_side)
t.end_fill()



t.done()