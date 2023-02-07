# Программа вычисляет значение функции (на вход - вещественное число)
import math


def func(x):
    if 0.2 <= x <= 0.9:
        x = math.sin(x)
        print(x)
    else:
        x = 1
        print(x)


value = float(input('Введите вещественное число:'))
func(value)
