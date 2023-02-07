# переменное число параметров
# *все позиционные аргументы будут собраны в кортеж
# **все ключевые аргументы будут собраны в словарь

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 1, 2, 3, vogetables=50, fruits=100))
