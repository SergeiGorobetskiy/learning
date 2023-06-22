# Напишите класс SquareFactory с одним
# статическим методом, принимающим единственный
# аргумент — сторону квадрата.
# Данный метод должен возвращать объект класса
# Square с переданной стороной.
class SquareFactory:
  @staticmethod
  def create_square(side):
     return Square(side)