# Подсчитать сумму цифр в вещественном числе.

import os
os.system('cls||clear')

num = (input("Enter the number >> "))

sum = 0
for i in num:
    if i == '-' or i == '.' or i == ',':
        continue 
    sum += int(i)
print(sum)