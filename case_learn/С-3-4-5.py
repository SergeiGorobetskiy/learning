# Дан файл numbers.txt,
# компоненты которого являются действительными числами
# (файл создайте самостоятельно и заполните любыми числам,
# в одной строке одно число). Найдите сумму наибольшего и
# наименьшего из значений и запишите результат в файл output.txt.
filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
   min_ = max_ = float(f.readline())  # считали первое число
   for line in f:
       num =  float(line)
       if num > max_:
           max_ = num
       elif num < min_:
           min_ = num

   sum_ = min_ + max_

with open(output, 'w') as f:
   f.write(str(sum_))
   f.write('\n')