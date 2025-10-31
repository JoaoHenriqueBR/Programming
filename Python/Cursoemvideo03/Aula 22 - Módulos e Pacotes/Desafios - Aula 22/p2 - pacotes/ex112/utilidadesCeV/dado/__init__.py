def leiaDinheiro(msg):
    erro = '\033[1;31mValor Inválido! Tente novamente.\033[m'

    while True:
        r = str(input(msg)).strip().replace(',','.')

        if r.isalpha() or r == '':
            print(erro)
        else:
            r = float(r)
            break
    return r

