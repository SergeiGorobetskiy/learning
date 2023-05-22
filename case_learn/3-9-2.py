# #
# Поправьте код так, чтобы он завершался,
# как только будет найден первый отрицательный элемент списка.
# Укажите позицию, куда нужно вставить break.
#1
list_ = [1,2,3,-1,3,2,1,2,3,2,1,0,0,0,-1,2]
#2
negate_index = -1
#3
negate_value = 0
#4
for i, val in enumerate(list_):
#5
   if val < 0:
       #6
       negate_index = i
       break
       #7
       negate_value = val
       #8
       break
    #9
print(f'{negate_index}: {negate_value}')