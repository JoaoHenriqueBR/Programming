"""
Reescreva a função leiaint() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33mOperação cancelada! Valor anulado.\033[m')
            return 0


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33mOperação cancelada! Valor anulado.\033[m')
            return 0


inteiro = leiaint('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você digitou {inteiro} e {real}.')
