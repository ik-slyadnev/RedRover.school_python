# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

import math



def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2 * (side ** 2))
    return (perimeter, area, diagonal)

print(square(5))