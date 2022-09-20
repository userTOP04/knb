import random


user_money = 100
casino_money = 1000


while user_money and casino_money:

    print("У игрока", user_money, "монет")
    print("У казино", casino_money, "монет")
    input("Нажмите ENTER чтобы сделать ход")

    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)


    print("Игрок выбросил", user_turn)
    print("Казино выбросил", casino_turn)


    if casino_turn > user_turn:
        print("Казино победил")
        user_money -= 1
        casino_money += 1
    elif casino_turn < user_turn:
        print("Игрок победил")
        user_money += 1
        casino_money -= 1
    else:
        print("Ничья")


if casino_money == 0:
    print("Конец. У казино кончилось дeньги")
else:
    print("Конец. У игрока кончилось дeньги")
