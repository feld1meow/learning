def find_smallest(arr):
    """"Функция для поиска наименьшего элемента массива"""
    smallest = arr[0]  # для хранения наименьшего значения
    smallest_index = 0  # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sort_by_selection(arr):
    """Функция сортировки выбором"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # находит наименьший элемент в массиве
        new_arr.append(arr.pop(smallest))  # и добавляет его в новый массив, удаляя из старого
    return new_arr


print('Array before sorting [5, 3, 11, 6, 9, 2, 10, 12, 8, 1, 4, 7]')
print('Array after sorting', sort_by_selection([5, 3, 11, 6, 9, 2, 10, 12, 8, 1, 4, 7]))
