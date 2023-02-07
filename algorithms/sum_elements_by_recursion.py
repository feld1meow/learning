def sum_recursion(array):
    """Функция вычисляет сумму
    элементов массива"""
    if not array:
        return 0
    return array[0] + sum_recursion(array[1:])


print(sum_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_recursion([-2, -1, 0]))
