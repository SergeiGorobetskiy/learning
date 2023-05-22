num = int(input(' введите число'))
digitToFind = 5

while num > 0:
   digit = num % 10
   if digit == digitToFind:
       print(f"{digitToFind} is in number {num}")
       break
   num = int(num / 10)