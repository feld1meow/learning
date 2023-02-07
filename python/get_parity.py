# Программа проверяет целое число на четность


def even(x):
    if x % 2 == 0:
        print(x, 'четное число')
    else:
        print(x, 'нечетное число')


value = int(input('Введите число:'))

even(value)
