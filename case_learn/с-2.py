# игра — тир. В этой игре
# пользователю нужно поражать цели,
# которыми будут выступать геометрические фигуры.
# Пусть это будут квадраты.

#класс позиции элемента, хранящий значения х и у
class Pos:
  def __init__(self, x, y) -> None:
      self.x = x
      self.y = y


#абстракция — класс произвольной фигуры с полями позиция и цвет
class Figure:
  def __init__(self, pos) -> None:
      self.setPos(pos)
      self.setColor(0)

  def setPos(self, pos):
     self.pos = pos

  def getPos(self):
     return self.pos

  def setColor(self,color):
     self.color = color

  def getColor(self):
     return self.color

   #метод, который намекает на “форму” — при выполнении метода класс возвращает True, если
   #точка, переданная х и у, лежит внутри фигуры и False в противном случае
   #поскольку класс Figure “не имеет” формы, то всегда возвращает False
  def isIn(self, x, y)->bool:
     return False


#класс прямоугольника с шириной и высотой
class Square(Figure):
  def __init__(self, pos , w, h) -> None:
     super().__init__(pos)
     self.w =  w
     self.h =  h


#isIn в этом случае возвращает True, если точка лежит между границами прямоугольника
  def isIn(self, x, y) -> bool:
     _pos = super().getPos()
     if (_pos.x < x) and ( (_pos.x + self.w) > x) and (_pos.y < y) and  ( (_pos.y + self.h) > y):
        return True
     return False