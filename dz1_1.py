def calculate_n(n):
  nn = int(str(n) * 2)
  nnn = int(str(n) * 3)
  result = n + nn + nnn
  return result

n = 11  # Замените значение на ваше целое число
result = calculate_n(n)
print(result)

def calculate_n(n):
  nn = n ** 2
  nnn = n ** 3
  result = n + nn + nnn
  return result

n = 5  # Замените значение на ваше целое число
result = calculate_n(n)
print(result)