# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()


text = input("Введите текст: ")
count = int(input("Введите количество повторений: "))

for i in range(count):
    print(text)

