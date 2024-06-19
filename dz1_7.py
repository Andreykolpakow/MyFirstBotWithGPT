def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

print("Выберите тип конвертации:")
print("1. Цельсии в Фаренгейты")
print("2. Фаренгейты в Цельсии")

choice = input("Введите номер операции (1/2): ")

if choice == '1':
  celsius = float(input("Введите температуру в градусах Цельсия: "))
  fahrenheit = celsius_to_fahrenheit(celsius)
  print("Температура в градусах Фаренгейта:", fahrenheit)
elif choice == '2':
  fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
  celsius = fahrenheit_to_celsius(fahrenheit)
  print("Температура в градусах Цельсия:", celsius)
else:
  print("Неверный выбор операции")