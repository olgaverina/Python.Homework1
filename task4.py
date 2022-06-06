# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import os
os.system('cls||clear')

n = int(input("Enter the number --> "))

arr = []

def create_array(array, num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i
        array.append(sum)
    return array

print(create_array(arr, n))
