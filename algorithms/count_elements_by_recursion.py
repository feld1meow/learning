def recursion_count_elements(list):
    """Функция вычисляет количество
     элементов списка"""
    if not list:
        return 0
    return 1 + recursion_count_elements(list[1:])


print(recursion_count_elements(['Hello', ',', 'World', '!']))
print(recursion_count_elements([1, 2]))
