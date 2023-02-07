def max_in_array(array):
    """"Функция находит наибольшее
    значение массива"""
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max_in_array = max_in_array(array[1:])
    return array[0] if array[0] > sub_max_in_array else sub_max_in_array


print(max_in_array([10, 20, 30, 40, 50, 60]))
print(max_in_array([-100, 0, 100]))
