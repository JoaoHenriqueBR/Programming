# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio;
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("~="*20)
print('FOGOS DE ARTIFICIO - CONTAGEM REGRESSIVA')
print("~="*20)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31m KABUUMM!!! \033[m')
