import random

print("1 - камень, 2 - ножницы, 3 - бумага")

# ход игрока
user_turn = int(input("Введите число от 1 до 3"))
if user_turn == 1:
    print("Игрок показал камень")
elif user_turn == 2:
    print("Игрок показал ножницы")
elif user_turn == 3:
    print("Игрок показал бумага")

# ход компа
computer_turn = random.randint(1, 3)
if computer_turn == 1:
    print("Компьютер показал камень")
elif computer_turn == 2:
    print("Компьютер показал ножницы")
elif computer_turn == 3:
    print("Компьютер показал бумага")


if user_turn == computer_turn:
    print("Ничья")
else:
    if user_turn == 1 and computer_turn == 2:
        print ("Игрок победил")
    elif user_turn == 2 and computer_turn == 3:
        print ("Игрок победил")
    elif user_turn == 3 and computer_turn == 1:
        print ("Игрок победил")


    else:
        print ("Компьютер победил")



