# Crie um código em Python que testa se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request


def acessivel():
    try:
        site = urllib.request.urlopen('https://www.pudim.com.br/')
    except urllib.error.URLError:
        print('Não foi possivel acessar o site do pudim.')
    else:
        print('Site acessado com sucesso!')
        print('\nBônus - Código do site: ')
        print(site.read())

acessivel()
