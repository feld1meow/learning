def binary_search(list, item):
    """Функция использует алгоритм бинарного поиска значения.
    Возвращает порядковый номер элемента в массиве."""
    low = 0  # нижняя граница части списка для поиска
    high = len(list)-1  # верхняя граница части списка для поиска

    while low <= high:  # пока эта часть не сократится до одного элемента
        # проверяем средний элемент
        # если mid нечетное, округляется в меньшую сторону
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:  # значение найдено
            return mid
        elif guess > item:  # много (guess != item)
            high = mid-1
        else:  # мало (guess < item)
            low = mid+1
    return  # значение не существует


my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_list2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search.__doc__)
print(binary_search(my_list1, 6))
print(binary_search(my_list1, 45))

print(binary_search(my_list2, 7))
print(binary_search(my_list2, 4))
