'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição).
'''

from datetime import date

info = dict()

info['nome'] = str(input('Digite o seu nome: '))
nasc = int(input('Ano em que nasceu: '))
info['idade'] = date.today().year - nasc
info['CTPS'] = int(input('Nº da Carteira de Trabalho (0 - Não tem): '))

if info['CTPS'] != 0:
    info['contratação'] = int(input('Ano de contratação: '))
    info['salário'] = float(input('Salário: R$ '))
    info['aposentadoria'] = (info['contratação']+35) - nasc # Minha versão
    # Versão do guanabara: info['aposentadoria'] = info['idade'] + ((info['contratação']+35) - date.today().year)
    
    print('-='*15)
    for k,v in info.items():
        print(f'{k}: {v}.')
else:
    for k, v in info.items():
        print(f'{k}: {v}.')
