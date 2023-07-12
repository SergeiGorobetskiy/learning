# Чтобы поработать с путями есть модуль os.
# Функция os.chdir() позволяет нам изменить директорию,
# которую мы в данный момент используем.
# Если вам нужно знать, какой путь вы в данный момент используете,
# для этого нужно вызвать os.getcwd().
import os
class Color:
    green = '\u001b[32m'
    red = '\u001b[31m'
    blue = '\u001b[34m'
def set_color(text, color):
    return color + text
# получить текущий путь
start_path = os.getcwd()
print(set_color('текущий путь ', Color.green) + start_path)
# подняться на один уровень выше
os.chdir('..')
os.getcwd()
print(set_color('текущий путь ', Color.red) + start_path)
# вернемся в ту директорию, из которой стартовали.
# Изначально мы сохраняли её в переменной start_path.
os.chdir(start_path)
os.getcwd()
print(set_color('текущий путь ', Color.blue) + start_path )

# список файлов и директорий в папке
print(os.listdir())
if 'tmp.py' not in os.listdir():
    print("Файл отсутствует в данной директории")