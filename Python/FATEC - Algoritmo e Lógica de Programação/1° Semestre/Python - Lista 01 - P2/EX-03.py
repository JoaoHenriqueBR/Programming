# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

from time import sleep
from math import trunc

a = 80000 # Cidade A
b = 200000 # Cidade B
c = 0


while a < b:
    ta = (a / 100)*3
    a = a + ta

    tb = (b / 100)*1.5
    b = b + tb

    c += 1
else:
    print(f'Com a cidade A tendo uma população de {trunc(a)} habitantes;\nCom a cidade B tendo {trunc(b)} habitantes; \nForam necessário {c} anos')
