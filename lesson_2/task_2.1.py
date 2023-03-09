# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.


persona = int(input())

if persona == 0 or persona < 0:
    print('False')
else:
    print('True')