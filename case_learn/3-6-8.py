# Олег положил тысячу рублей в банк под 8 % годовых.
# Через сколько лет у него на счёте будет
# не менее трёх тысяч рублей?
# Выведите на экран это число и запишите его в ответ.

deposit = 1000
year = 0
percent = 0.08
goal = 3000
while deposit < goal:
    deposit = deposit * float(1+percent)
    year +=1
print(year)
print(deposit)
