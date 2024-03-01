book_dict = {}
print("Введите название книги: ")
book_name = input()
print("Введите автора книги: ")
book_author = input()
book_dict[book_name] = book_author
print(f"Книга {book_name} от автора {book_author} добавлена в словарь.")

# Создание файла и запись информации в него
file_name = f"{book_name}.txt"
try:
    with open(file_name, 'w') as file:
        file.write(f"Книга: {book_name}\nАвтор: {book_author}")
except FileNotFoundError:
    print(f"Файл {file_name} не найден.")
