# Задача
# Впишите вместо знаков «?» операцию сравнения
# идентификаторов списков до и после обновления,
# чтобы программа распечатала True,
# если они равны, иначе — False.

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

print(shopping_center)
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(shopping_center)

print(list_id_before == list_id_after)
print(list_id_before)
print(list_id_after)
