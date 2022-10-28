import turtle as t
from PIL import ImageGrab


def build_house(base_x = -500, base_y = -500, base_width = 100, base_height = 10, base_fill = "#000000", walls_width = 20, walls_height = 20, walls_fill = "#000000", door_fill = "#b81f00", roof_width = 0, roof_height = 0, roof_fill = "#000000"):
    """
        base_x — X левого нижнего угла фундамента
        base_y — Y левого нижнего угла фундамента
        base_width — ширина фундамента
        base_height — высота фундамента
        base_fill — цвет заливки фундамента
        walls_x - считаем автоматически
        walls_y - считаем автоматически
        walls_width - спрашиваем у заказчика
        walls_height - спрашиваем у заказчика
        walls_fill - спрашиваем у заказчика
        roof_x - считаем автоматически
        roof_y - считаем автоматически
        roof_width - спрашиваем у заказчика
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
        door_x - считаем автоматически
        door_y -считаем автоматически
        door_width - стандартная (возможно в будущем, будем спрашивать у заказчика)
        door_height - стандартная (возможно в будущем, будем спрашивать у заказчика)
        door_fill - спрашиваем у заказчика
         
    """
    img = ImageGrab.grab()
    screen_width = img.size[0]
    screen_height = img.size[1]

    ts = t.getscreen()
    ts.screensize(screen_width, screen_height)

    t.speed(0)
    walls_x = base_x
    walls_y = base_y + base_height
    walls_width = base_width
    door_width = 75
    door_height = 100
    door_x = (walls_width - door_width) / 2 + base_x
    door_y = base_height + base_y   
    roof_x = walls_x - (walls_width * 0.1)
    roof_y = walls_y + walls_height
    roof_width = walls_width * 1.2



    def build_base(base_x, base_y, base_width, base_height, base_fill):
        print(f"The foundation team has arrived and is digging a foundation pit in {base_x} and {base_y}")
        t.penup()
        t.setheading(0)
        t.goto(base_x, base_y)
        t.pendown()
        t.fillcolor(base_fill)
        t.begin_fill()
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.end_fill()


    def build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill):
        print("brigade walls come")
        t.penup()
        t.setheading(0)
        t.goto(walls_x, walls_y)
        t.pendown()
        t.fillcolor(walls_fill)
        t.begin_fill()
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.end_fill()


    def build_door(door_x, door_y, door_width, door_height, door_fill):
        t.penup()
        t.setheading(0)
        t.goto(door_x, door_y)
        t.pendown()
        t.fillcolor(door_fill)
        t.begin_fill()
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.left(90)
        t.forward(door_width)                       
        t.left(90)
        t.forward(door_height)
        t.left(90)
        t.end_fill()



    def build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill):
        print("brigade roof come")
        print(walls_width / 2 + base_x, base_height + walls_height + roof_height + base_y)
        t.penup()
        t.goto(roof_x, roof_y)
        t.setheading(0)
        t.fillcolor(roof_fill)
        t.pendown()
        t.begin_fill()                                              
        t.forward(roof_width)
        t.goto(walls_width / 2 + base_x, base_height + walls_height + roof_height + base_y)
        t.goto(roof_x, roof_y)
        t.end_fill()


    build_base(base_x, base_y, base_width, base_height, base_fill)
    build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill)
    build_door(door_x, door_y, door_width, door_height, door_fill)
    build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill) 
    print("house construction completed")


build_house(base_x = -100, base_y = -40, base_width = 200, base_height = 10, base_fill = "#993300", walls_height = 160, walls_fill = "#e2e2e2", door_fill = "#b81f00", roof_height = 100, roof_fill = "#fba67f")
build_house(base_x = 150, base_y = -330, base_width = 300, base_height = 50, base_fill = "#993300", walls_height = 1700, walls_fill = "#e2e2e2", door_fill = "#b81f00", roof_height = 160, roof_fill = "yellow")
build_house(base_x = 400, base_y = -340, base_width = 200, base_height = 1, base_fill = "#993300", walls_height = 160, walls_fill = "#e2e2e2", door_fill = "#b81f00", roof_height = 410, roof_fill = "orange")      
build_house(base_x = -350, base_y = -320, base_width = 300, base_height = 15, base_fill = "#993300", walls_height = 190, walls_fill = "#e2e2e2", door_fill = "#b81f00", roof_height = 120, roof_fill = "black")
build_house(base_x = -600, base_y = -320, base_width = 200, base_height = 5, base_fill = "#993300", walls_height = 360, walls_fill = "#e2e2e2", door_fill = "#b81f00", roof_height = 110, roof_fill = "red")
t.done()