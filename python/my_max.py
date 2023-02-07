# Программа определяет максимальное из двух введенных чисел
# без использования стандартной функции max


def max_value(x, y):
    if x > y:
        print(x, 'больше, чем', y)
    else:
        print(y, 'больше, чем', x)


value1 = int(input('Введите первое число:'))
value2 = int(input('Введите второе число:'))

max_value(value1, value2)
