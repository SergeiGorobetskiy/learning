# генератор цикла
#data = [1, 2, 3, 4, 5]
#for item in range(0, len(data)):
#     print(item, '   ',data[item])

# while условие:
#n = 0
#while n < 11:
#    print(n)
#    n= n + 1

# задача 4
#data = []
#num = int(input('введите числа')) #34
#while num !=0: #0 !=0 это ошибка и поэтому цикл завершается
#    data.append(num) #data = [34]
#    num = int(input('введите числа'))
#data.sort()
#print(data)

#задача 5
#words = []
#word = input('введите слово')
#while word != '':
#    if word not in words:
#        words.append(word)
#    word = input('введите слово')
#for item in words:
#    print(item)

#задача 6
#negatives = []
#positive = []
#zeros = []
#line = input('введите целое число ')
#while line != '':
#    num = int(line)
#    if num < 0:
#        negatives.append(num)
#    elif num > 0:
#        positive.append(num)
#    else:
#        zeros.append(num)
#    line = input('введите целое число')
#for n in negatives:
#    print(n, end=' ')
#for n in zeros:
#    print(n, end=' ')
#for n in positive:
#    print(n, end=' ')

#Задача 7
#num = int(input('введите число')) #10
#maxs = 0
#while num!= 0:
#    if num % 5 == 0 and maxs < num: #10<25
#        maxs = num
#    num = int(input('введите число')) #25
#print(maxs)

# Задача 8