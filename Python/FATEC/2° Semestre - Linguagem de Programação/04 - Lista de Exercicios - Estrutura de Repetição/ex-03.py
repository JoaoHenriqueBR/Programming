# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela. 

from time import sleep

print("~="*20)
print('FOGOS DE ARTIFICIO - CONTAGEM REGRESSIVA')
print("~="*20)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31mFOGO!!! \033[m')
