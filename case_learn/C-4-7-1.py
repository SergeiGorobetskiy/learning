# найти индекс определенного элемента в массиве.
# В связи с тем, что алгоритм может искать только в отсортированном
# массиве, используем генератор последовательных чисел range.
# Суть двоичного поиска сводится к тому,
# что на каждой итерации размер исследуемого массива
# уменьшается в 2 раза.

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 98))