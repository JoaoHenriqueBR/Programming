'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

gols = list()
jogador = {'nome':str(input('Nome do jogador: ')),
           'gols':gols}

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))

jogador['total'] = sum(gols)
print('-='*20)
print(jogador)
print('-='*20)

for k, v in jogador.items():
    print(f'{k}: {v}')

print('-='*20)

print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
