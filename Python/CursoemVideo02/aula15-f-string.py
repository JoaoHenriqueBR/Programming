'''
F-STRINGS (Evolução Python 2 -> Python 3.6+)
'''

nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.') # PYTHON 3.6+

print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
