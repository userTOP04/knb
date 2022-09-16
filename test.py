import random
user_turn = int(input("Введите число: 1 - камень, 2 -ножницы или 3 - бумага"))
computer_turn = random.randint(1, 3)

print("Игрок показал", user_turn)
print("Компьютер показал", computer_turn)


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



