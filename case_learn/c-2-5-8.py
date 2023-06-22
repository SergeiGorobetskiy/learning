#класс, представляющий квадрат
class Square:
    _a = None


    #конструктор с параметром a
    def __init__(self, a):
        if a > 0:
            self._a = a


    #создаем свойство a при помощи декоратора
    @property
    def a(self):
        return self._a


    #указываем сеттер для свойства
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value