# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print('Começa com o nome "SANTO"? {}'.format(cidade.upper().startswith('SANTO')))
