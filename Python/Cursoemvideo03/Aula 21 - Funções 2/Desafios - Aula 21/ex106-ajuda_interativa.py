'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
'''

from time import sleep # Bibliotecas importadas

# Variável global com as cores
c = (
    '\033[m',           # 0 - Sem cores
    '\033[0;30;41m',    # 1 - Vermelho
    '\033[0;30;42m',    # 2 - Verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m'        # 6 - branco
)


# Funções
def ajuda(cmd):
    título(f'Acessando  o manual do comando \'{cmd}\'', 4)
    print(c[6])
    help(cmd)
    print(c[0], end='')
    sleep(2)


def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal    
while True:
    título('SISTEMA DE AJUDA PyQuickHELP', 2)
    cmd = input('Digite o comando (FIM para parar): ')
    if cmd.upper().strip() == 'FIM':
        break
    
    ajuda(cmd)

título('ATÉ LOGO MEU CONSAGRADO! :)', 1)
