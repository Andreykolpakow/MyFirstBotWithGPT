from fractions import Fraction

# Преобразование вещественного числа в дробь
fraction = Fraction('14.375')

# Вывод дроби в формате '14.375 = числитель/знаменатель'
print(f'{float(fraction):.3f} = {fraction.numerator}/{fraction.denominator}')