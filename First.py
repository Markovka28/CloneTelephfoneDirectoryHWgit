import random

def multiply_random_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    result = num1 * num2
    output = f"{num1} * {num2} = {result} - это умножение для первого commit"
    print(output)
    return output

multiply_random_numbers()