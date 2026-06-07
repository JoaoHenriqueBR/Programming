import math
import os
import random
import re
import sys

#
# Complete the 'romanizer' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def romanizer(numbers):
    # Write your code here
    romans = ('I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M')
    arabics = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
    array = []
    for n in numbers:
        result = []
        r = ''
        for i in range(len(arabics)-1, -1, -1):
            if n >= arabics[i]:
                c = int(n / arabics[i])
                result.append(romans[i]*c)
                n -= arabics[i]*c
            r = ''.join(result)
        array.append(r)
            
    return array
            

if __name__ == '__main__':

    numbers_count = int(input('Numbers quantity: ').strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input(f'Number {_}: ').strip())
        numbers.append(numbers_item)

    result = romanizer(numbers)

    print(result)
