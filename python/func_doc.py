def print_max(x, y):
    """Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами."""
    x = int(x)  # конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


print_max(3, 5)
print(print_max.__doc__)
help(print_max)
