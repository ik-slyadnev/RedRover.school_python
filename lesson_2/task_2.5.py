# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите оператор (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Оператор не распознан. Пожалуйста, введите оператор из списка (+, -, *, /).")
    result = None

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")