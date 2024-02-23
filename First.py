import random

def multiply_random_numbers():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    res = a * b
    out = f"{a} * {b} = {res} - это умножение для первого commit"
    print(out)
    return out
multiply_random_numbers()

