import ramdom
print("Угадай число от 1 до 100 ")
secret = random.randint(1, 100)
attempts = 7

while attempts:
    print(f"Осталось {attempts} попыток")
user_choice = int(input("Введите число от 1 до 100"))
if user_choice == secret:
    print(Правильно)
elif user_choice > secret:
    attempts -= 1
    print ("Многовато")
else:
    print("Маловато")
    attempts -= 1