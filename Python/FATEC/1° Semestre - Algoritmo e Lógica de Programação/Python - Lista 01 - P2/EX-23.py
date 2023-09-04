'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

a. Código da cidade;

b. Número de veículos de passeio (em 1999);

c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:

d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;

e. Qual a média de veículos nas cinco cidades juntas;

f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

from os import system
from math import inf
maior = 0
menor = inf
acid_media = 0
media = 0
cid = 0

for c in range(5):
    print('{} CIDADE {} - 1999 {}'.format('-'*5, c+1, '-'*5))
    status = 'erro'
    while status == 'erro':
        try: 
            cod = int(input('Código da Cidade: '))
            veic = int(input('Número de veículos de passeio: '))
            acid = int(input('Número de acidentes de trânsito com vitimas: '))
        except:
            veic = -1
            acid = -1
            pass
        if veic >= 0 and acid >= 0:
            if acid/veic > maior:
                maior = acid/veic
                cod_maior = cod
            if acid/veic < menor:
                menor = acid / veic
                cod_menor = cod
            if veic < 2000:
                acid_media += acid
                cid += 1
            media += veic
            break
        system('clear')
        print('Valor Inválido! Tente novamente.\n')

system('clear')
print(f'Maior indice de acidente: Cidade {cod_maior} - {maior} acidentes / veiculo')
print(f'Menor indice de acidente: Cidade {cod_menor} - {menor} acidentes / veiculo')
print('Média de veículos: {:.0f} veiculos/cidade'.format(media/(c+1)))
print('Média de acidentes em cidades de menos de 2000 veiculos: {:.0f} acidentes'.format(acid_media/cid))
