# должен содержать число Пи в виде константы 3.14
# и две функции, которые будут считать площадь круга
# и прямоугольника.
# модуль 1
module_name import *
PI = 3.14

def circle_area(r):
   return PI * (r ** 2)


def rect_area(a, b):
   return a * b


if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert circle_area(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
   assert rect_area(5, 4) == 20

# модуль 2

from module_name import *

def main():
r = int(input('Введите радиус круга:\n'))

a = int(input('Введите длину прямоугольника:\n'))
b = int(input('Введите ширину прямоугольника:\n'))
if circle_area(r) > rect_area(a, b):
print('Площадь круга больше')
else:
print('Площадь прямоугольника больше')

if name == 'main':
main()