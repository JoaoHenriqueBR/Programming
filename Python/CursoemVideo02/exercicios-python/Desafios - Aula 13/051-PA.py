# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('O primeiro termo da PA: '))
r = int(input('A razão da PA: '))
f = a1 + (10-1)*r

for c in range(a1, f+1, r ):
    print(c)
