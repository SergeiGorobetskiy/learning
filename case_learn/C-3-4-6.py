# В текстовый файл построчно записаны фамилии и имена
# учащихся класса и их оценки за контрольную.
# Выведите на экран всех учащихся,
# чья оценка меньше 3 баллов. Cодержание файла:
with open('C-3-4-6-input.txt', encoding="utf8") as file:
    for line in file:
        points = int(line.split()[-1])
        if points < 3:
            name = " ".join(line.split()[:-1])
            print(name)