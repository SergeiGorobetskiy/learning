# Задача
# Модифицируйте алгоритм из предыдущей задачи,
# чтобы найти первое отрицательное число, не хранящееся в кэше.
# Какое число получилось здесь?

a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)