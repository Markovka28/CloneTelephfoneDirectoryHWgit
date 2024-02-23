import random
def random_word_from_list(number):
    word_list = ["яблоко", "банан", "вишня", "киви", "груша", "арбуз"]
    
    if number < 1 or number > len(word_list):
        return "Неверный ввод. Пожалуйста, введите число в пределах диапазона из списка"
    random_word = random.choice(word_list)
    return random_word

number = int(input("Введите номер: "))
result = random_word_from_list(number)
print(result)