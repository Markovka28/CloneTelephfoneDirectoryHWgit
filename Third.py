import random

# Создание массива с буквами русского алфавита
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Функция для генерации случайного слова из заданной длины
def generate_random_word(length):
    random_word = ''
    for _ in range(length):
        random_word += random.choice(alphabet)
    return random_word

# Генерация и вывод случайных слов
for _ in range(5):  # Генерируем 5 случайных слов
    random_word = generate_random_word(random.randint(5, 10))  # Генерируем слова длиной от 5 до 10 символов
    print(random_word)