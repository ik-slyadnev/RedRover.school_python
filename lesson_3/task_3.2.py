# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'


list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
summa = 0

for item in list_1:
    if isinstance(item, int):
        summa += item

print(summa)


for item in list_1:
    if isinstance(item, str) and item.find('a') != -1:
        print(item)