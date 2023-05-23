# При помощи генератора списков создайте таблицу
# умножения чисел от 1 до 10.
T = [[i*j for j in range(1,11)] for i in range(1,11)]
print(T)
L = [input() for i in range(5)]
print(L)