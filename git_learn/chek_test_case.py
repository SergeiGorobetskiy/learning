#words = []
#word = input('введите слово')
#while word != '':
#    if word not in words:
#        words.append(word)
#    word = input('введите слово')
#for item in words:
#    print(item)

#задача 6
negatives = []
positive = []
zeros = []
line = input('введите целое число ')
while line != '':
   num = int(line)
   if num < 0:
       negatives.append(num)
   elif num > 0:
       positive.append(num)
   else:
       zeros.append(num)
   line = input('введите целое число')
for n in negatives:
   print(n, end=' ')
for n in zeros:
   print(n, end=' ')
for n in positive:
   print(n, end=' ')