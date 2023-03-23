# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль невозможно")
    return x / y