def check_even_odd(num):
    if num % 2 == 0:
        return "Число {} является четным".format(num)
    else:
        return "Число {} является нечетным".format(num)

try:
    num = int(input("Введите целое число: "))
    result = check_even_odd(num)
    print(result)
except ValueError:
    print("Ошибка: Введено не целое число")