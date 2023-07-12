# измеритель времени исполнения нашего кода:
from datetime import datetime
import time  # проверять действие измерителя будем с помощью библиотеки time


# вся суть этого измерителя заключается в том, что мы считаем разницу в секундах между открытием и закрытием контекстного менеджера
class Timer:
    def __init__(self):
        pass

    def __enter__(
            self):  # этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто верните этот объект через return
        self.start = datetime.utcnow()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
        print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")


with Timer():
    time.sleep(2)  # засыпаем на 2 секунды