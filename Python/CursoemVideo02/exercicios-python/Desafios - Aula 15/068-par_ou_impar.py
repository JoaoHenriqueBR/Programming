# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-'*10)
print('PAR OU ÍMPAR?')
print('=-'*10)

wins = 0

while True:
    cpu = randint(0, 10)
    player = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()
    resultado = cpu + player
    print('-'*30)
    if resultado % 2 == 0:
        print(f'Você jogou {player} e o computador {cpu}. Total de {resultado} - DEU PAR!')
        resultado = 'P'
    else:
        print(f'Você jogou {player} e o computador {cpu}. Total de {resultado} - DEU ÍMPAR!')
        resultado = 'I'
    print('-'*30)
    if resultado == escolha:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        wins += 1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Você venceu {wins} vezes.')
        break

