import math
import os
import random
import re
import sys

def getOneBits(n):
    # Write your code here
    binary = bin(n)
    c = 0
    array = []
    for i, b in enumerate(binary):
        if i >= 2:
            if b == "1":
                array.append(i-1)
                c += 1
    array.insert(0, c)
    return array
            

if __name__ == '__main__':

    n = int(input("Digite um número: ").strip())

    result = getOneBits(n)

    print(f"Quantidade de 1 em binário: {result[0]}")
    print(f"Posição do 1 em binário: {result[1:]}")
