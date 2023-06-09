#  Напишите декоратор, который будет сохранять результаты
#  выполнения декорируемой функции в словаре.
#  Словарь должен находиться в nonlocal области
#  в следующем формате: по ключу располагается аргумент функции,
#  по значению результат работы функции,
#  например, {n: f(n)}.
#
# И при повторном вызове функции будет брать значение из словаря,
# а не вычислять заново.
# То есть словарь можно считать промежуточной памятью
# на время работы программы,
# где будут храниться ранее вычисленные значения.
# Исходная функция, которую нужно задекорировать имеет следующий
# вид и выполняет простое умножение на число 123456789.:

def f(n):
   return n * 123456789

def cache(func):
   cache_dict = {}
   def wrapper(num):
       nonlocal cache_dict
       if num not in cache_dict:
           cache_dict[num] = func(num)
           print(f"Добавление результата в кэш: {cache_dict[num]}")
       else:
           print(f"Возвращение результата из кэша: {cache_dict[num]}")
       print(f"Кэш {cache_dict}")
       return cache_dict[num]
   return wrapper