'''
Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

gols = list()
jogador = dict()
time = list()

while True:
    jogador.clear()
    gols.clear()

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    time.append(jogador.copy())

    while True:
        r = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break

print('-='*30)
print('cod ', end='')
for c in jogador.keys():
    print(f'{c:<15}', end='')
print()
print('-'*40)
for c, j in enumerate(time):
    print(f'{c:>4} ', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*40)

while True:
    c = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if c == 999:
        break
    if c >= len(time):
        print(f'ERRO! Não existe jogador com o código {c}.')
    else:
        print(f'LEVANTAMENTO DE DADOS DO JOGADOR: {time[c]["nome"]}')
        for i, g in enumerate(time[c]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')  
