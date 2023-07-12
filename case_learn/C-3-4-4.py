# пример создать любой файл на операционной системе
# под название input.txt
# и построчно перепишите его в файл output.txt.
with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in input_file:
           output_file.write(line)