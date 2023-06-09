user_peter = {
    "name": "Peter",
    "email": "peterrobertson@mail.com",
    "created_at": "2019-05-05",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
}

user_julia = {
    "name": "Julia Donaldson",
    "email": "juliadonaldson@mail.com",
    "created_at": "2019-06-13",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Magic Brush"],
}

product_eggs = {
    "name": "Egg",
    "category": "food",
    "is_available": False,
    "quantity_in_stock": 0,
    "vendor": "Dark Knight LTD",
    "manager": "William The Conqueror",
}


def is_product_available(product):
    return True if product["quantity_in_stock"] > 0 else False

class User:
    pass  # этот класс ничего не делает
class User:
    pass

peter = User()
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)

class User:
    number_of_fingers = 5
    number_of_eyes = 2

lancelot = User()
print(lancelot.number_of_fingers)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
# После того, как мы задали конструктор,
# при создании объектов в скобки вызова класса можно передавать
# аргументы, которые он принимает на вход. Чтобы не запутаться,
# можно явно указать, в какой аргумент что класть:
peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)

class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False
eggs = Product("eggs", "food", 5)
print(eggs.is_available())
class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)


    class Event:
        def __init__(self, timestamp=0, event_type="", session_id=""):
            self.timestamp = timestamp
            self.type = event_type
            self.session_id = session_id


# Пример неправильного кода

# Создаём неправильный класс.
class Human:
    # класс человек с полем возраста
    age = None

    def __init__(self, age=4):
        self.age = age


h = Human()
h.age = 15  # (Так делать лучше не стоит, если вы хотите когда-нибудь найти работу)
print(h.age)  # и так тоже


# Более правильный пример

# Исправим наш предыдущий код.
class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age,
                                  int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age


h = Human()
h.set_age(15)
print(h.get_age())

import datetime


class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)

print(eggs.is_available())


class MyClass():
    def f(self):
        return 155


if __name__ == "__main__":
    mc = MyClass()
    print("It's only for test", mc.f())


    class MyClass():
        def f(self):
            return 155


    mc2 = MyClass()
    print("It's for test too", mc2.f())

    if __name__ == "__main__":
        mc = MyClass()
        print("It's only for test", mc.f())

from myclass import MyClass
if __name__ == "__main__":
   m=MyClass()
   print("It's really working:",m.f())

class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)