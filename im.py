import os
import random


name = input("Как вас зовут? ")
if not name:
    name = "Илья"

# настройка
way_1 = True
way_2 = True
way_3 = True
game = True
key = ""

while game:

    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")
        print(f"Подъезжает {name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть")
        if way_1:
            print("1 - Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь")
        if way_2:
            print("2 - Ну, поеду теперь, где женатому быть")
        if way_3:
            print("3 - Ну, поеду теперь в дорожку, где богатому быть")

        user_choice = input("Введите номер ответа и нажмите ENTER ")
        key += user_choice

    # дорога 1 - разбойники
    if way_1 and key == "1":
        os.system("cls")
        print("Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь")
        print("1 - Сразиться с разбойники")
        print("2 - Вступить в банду к разбойникам")

        user_choice = input("Введите номер ответа и нажмите ENTER ")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if way_1 and key == "11":
        os.system("cls")
        print("Текст дорога 1 - Сразитесь с разбойниками")
        user_hp = 50
        rb_hp = 50
    while user_hp and rb_hp:
        user_ud = random.randint(1, 5)
        rb_ud = random.randint(1, 5)
        print("Нажмите ENTER для удара")
        rb_hp -= user_ud
        print(f"{name} ударил разбойника")
        print(rb_hp)
        user_hp -= rb_ud
        print(f"разбойник убарил {name}")
        print(user_hp)
        wait = input("Для продолжения нажмите ENTER")
        print("Для продолжения нажмите ENTER")
        if rb_hp <= 0:
            print(" У разбойника кончилось жизни")
        else:
            print(f" У {name} жизни")
            way_1 = False
            key = ""




if way_1 and key == "12":
    os.system("cls")
    print(f"Текст дорога 1 - Предали разбойники {name} и убили его ночью ")
    game = False
    print("Нажмите ENTER для продолжения")


    # дорога 2 - княжнаdfasdf
    if way_2 and key == "2":
        os.system("cls")
        print("Ну, поеду теперь, где женатому быть")
        print("1 - Предать королеву и проверить кровать а потом убить ее ")
        print("2 - Остаться с королевой и пойти спать")

        user_choice = input("Введите номер ответа и нажмите ENTER ")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if way_2 and key == "21":
        os.system("cls")
        print("Текст дорога 2 - Кровать оказалась ловушкой там было много князей и богатырей вы отпустили их , убили королеву и он вернулся к белому камню, стер старую надпись, новую написал Ездил в правую дорожку убит не был")
        way_2 = False
        key = ""
        print("Нажмите ENTER для продолжения")


    if way_2 and key == "22":
        os.system("cls")
        print("Текст дорога 2 - Кровать оказалась ловушкой и вы остались гнить в ее подземельи")
        game = False
        print("Нажмите ENTER для продолжения")



    # дорога 3 - богатство
    if way_3 and key == "3":
        os.system("cls")
        print("Ну, поеду теперь в дорожку, где богатому быть")
        print("1 - Сдвинуть камень и открыть сундук")
        print("2 - Уехать отуда")


        user_choice = input("Введите номер ответа и нажмите ENTER ")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if way_3 and key == "31":
        os.system("cls")
        print("Текст дорога 1 - Вы нашли много сокровищ и отвезли и раздали бедным")
        way_3 = False
        key = ""
        print("Нажмите ENTER для продолжения")



    if way_3 and key == "32":
        os.system("cls")
        print("Текст дорога 3 - Вы уехали отуда но потому что вы не сдвинули камень снеба упала гигантская скала и раздавила вас")
        game = False
        print("Нажмите ENTER для продолжения")


    if way_1 == way_2 == way_3 == False:
        os.system("cls")
        print("Все дороги проехал молодец игра пройдена WIN")
        game = False

print("Конец")