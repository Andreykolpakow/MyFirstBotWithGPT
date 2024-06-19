numbers = [1, 2, 3, 4, 5, 6, 237, 8, 10, 12]  # Пример заданного списка чисел

for num in numbers:
    if num == 237:
        break
    if num % 2 == 0:
        print(num)