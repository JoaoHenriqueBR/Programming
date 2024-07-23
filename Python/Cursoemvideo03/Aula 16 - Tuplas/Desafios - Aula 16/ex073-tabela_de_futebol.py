'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em Ordem Alfabética.
D) Em que posição da tabela está o time do Cuiabá. <-- O Time original do video, Chapecoense está na série B em 2024
'''

tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'São Paulo', 'Bahia', 'Cruzeiro', 'Athletico-PR', 'Bragantino', 'Atlético-MG', 'Vasco', 'Juventude', 'Internacional', 'Corinthians', 'Criciúma', 'Cuiabá', 'Vitória', 'Grêmio', 'Fluminense', 'Atlético-GO')

print('='*20)
print(f'{"BRASILEIRÃO 2024":^20}')
print('='*20)
for pos, time in enumerate(tabela):
    print(f'{pos+1}º - {time}')
print('')
print('-> 22 de julho de 2024')


print('-'*20)
print(f'5 Primeiros colocados: {tabela[:5]}')
print('')
print(f'Últimos 4 colocados: {tabela[-4:]}')
print('')
print(f'Ordem Alfabética: {sorted(tabela)}')
print('')
print(f'Cuiabá está na {tabela.index("Cuiabá")+1}ª posição')
print('-'*20)

