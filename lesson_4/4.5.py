# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@calculate_time
def my_function():
    time.sleep(2)
    print("Функция выполнена")

my_function()