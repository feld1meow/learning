def printMax(a, b):
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'equal', b)
    else:
        print(b, 'max')


printMax(3, 4)  # прямая передача значений

x = 5
y = 7

printMax(x, y)  # передача переменныъ в качестве аргумента
