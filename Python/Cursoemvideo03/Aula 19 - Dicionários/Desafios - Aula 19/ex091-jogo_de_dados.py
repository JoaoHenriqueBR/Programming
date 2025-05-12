'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'player1' : randint(1,6),
           'player2' : randint(1,6),
           'player3' : randint(1,6),
           'player4' : randint(1,6)}
ranking = dict()

print('Valores sorteados: ')
sleep(1)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*15)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}. ')
    sleep(1)
