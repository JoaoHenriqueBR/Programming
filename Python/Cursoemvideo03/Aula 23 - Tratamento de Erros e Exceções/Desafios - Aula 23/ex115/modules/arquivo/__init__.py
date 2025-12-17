from time import sleep

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(',')
            dado[1] = dado[1].replace('.\n', '')
            print(f'{dado[0]:<22}{dado[1]:>3} anos')
        a.close()

def escreverArquivo(arquivo, nome, idade ):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[0;31mErro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome}, {idade}.\n')
        except:
            print('\033[0;31mHouve um erro ao escrever os dados!\033[m')
        else:
            print(f'{nome} foi adicionado(a) com sucesso.')
            sleep(0.5)
            a.close()

