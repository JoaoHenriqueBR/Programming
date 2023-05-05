# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora,
# utilizando o laço for.

n = int(input('Número que deseja saber a tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
