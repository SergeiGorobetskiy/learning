# Модифицируйте пример таким образом,
# чтобы в список сохранялось True, если элемент четный,
# и False, если элемент нечетный.
# L = [int(input()) for i in range(5)]
L = [int(input()) % 2 == 0 for i in range(5)]
print(L)