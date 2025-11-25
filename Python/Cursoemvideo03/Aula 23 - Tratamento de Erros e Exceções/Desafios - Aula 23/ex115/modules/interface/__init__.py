from time import sleep
from ..arquivo import lerArquivo, escreverArquivo

def separador(tam = 30):
    print('-'*tam)


def titulo(txt):
    separador(30)
    print(f'{txt:^30}')
    separador(30)


def menu(opcoes=None):
    """
        Exibe um menu interativo contendo uma lista de opções.
    """

    if opcoes is None:
        opcoes = []
    titulo('MENU PRINCIPAL')
    
    for c, item in enumerate(opcoes):
        print(f'\033[33m{c+1} -\033[m \033[34m{item}\033[m')

    separador()

    n = leiaint('\033[32mEscolha:\033[m ')
    return n


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33mPrograma Encerrado!\033[m')
            return 3



def escolha(n, arquivo):
    """
        Define o resultado de cada escolha.

        :param n: Opção escolhida.
        :param arquivo: Arquivo usado como base.
    """


    while True:
        if n == 1:
            # Opção de listar o conteúdo de um arquivo
            titulo('PESSOAS CADASTRADAS')
            lerArquivo(arquivo)
            break
        elif n == 2:
            titulo('CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            escreverArquivo(arquivo, nome, idade)
            break
        elif n == 3:
            titulo('Saindo do sistema...')
            sleep(0.5)
            break
        else:
            print('\033[31mOpção não existe, tente novamente.\033[m')
            sleep(1)
            break
