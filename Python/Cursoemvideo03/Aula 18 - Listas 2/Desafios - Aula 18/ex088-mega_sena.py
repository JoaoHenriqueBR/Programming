'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

print('-'*35)
print(f'{"JOGA NA MEGA SENA":^36}')
print('-'*35)

r = int(input('Nº de jogos: '))
jogos = list()
jogo = list()

for i in range(0,r):
  for c in range(0, 6):
    jogo.append(randint(1, 60))
  jogos.append(jogo[:])
  jogo.clear()

print('='*35)
print(f'{"Jogos sorteados":^35} ')
print('='*35)
for c, i in enumerate(jogos):
  print(f'Jogo {c+1}: {i}')
  sleep(1)

print('-='*5, '< BOA SORTE >', '-='*5)
