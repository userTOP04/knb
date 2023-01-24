import random

mushrooms = 0
spray = 20


while True:
	if spray < 1:
		print("Спрей от комаров закончился!")
		print(f"Корзина: {mushrooms}/{100}")
		print("Спрей: 0/20")
		break
	if mushrooms >= 100:
		print("Корзина полна!")
		print("Корзина: 100/100")
		print(f"Спрей: {spray}/{20}")
		break
	print("Поиск грибов...")
	mushrooms_found = random.randint(0, 100)
	print("Найдены грибы:", mushrooms_found)
	mushrooms += mushrooms_found
	if mushrooms > 100:
		mushrooms = 100
	print("Осталось места в корзине:", 100 - mushrooms)
	print(f"Корзина: {mushrooms}/{100}")
	spray -= 1
	print(f"Спрей: {spray}/{20}")

