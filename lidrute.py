LIBRARY = []


book_numders = 1

def add_book():
	print("Добовляем книшу")

	title = input("Введите название книги:")
	if not title:
		print("Ошибка не указано название")
		return
	author = input("Введите имя Автора: ")
	if not author:
		print("Ошибка не указано Автор")
		return
	year = input("Введите год издания: ")
	if not year:
		print("Ошибка не указан год издания")
		return
		if year.isdigit():
			year = int(year)
		else:
			print("Ошибка! Год должен быть цельным числом")
			return


	book = {
		"Название": title,
		"Автор": author,
		"Год": year
	}


	LIBRARY.append(book, book_numders)
	print(f"Книга {title} {author} {year} успешно добавлена в библиотеку ")
	book_numders += 1


def show_books():
	for num, book in enumirate(LIBRARY, 1):
		print("Номер на полке", num)
		print("Название", book["название"])
		print("Автор", book["автор"])
		print("Год", book["год"])

add_book()
show_books()