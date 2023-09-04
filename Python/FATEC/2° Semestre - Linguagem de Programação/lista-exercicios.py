'''
Instruções
- Declare uma variável chamada cidade e atribua a ela o nome da sua cidade natal. 
- Crie uma variável idade e atribua a sua idade como um número inteiro. 
- Crie uma variável pi e atribua o valor de π (pi) como um número de ponto flutuante. 
- Declare uma variável verdade e atribua a ela o valor True. 
- Imprima o tipo de cada uma das variáveis criadas usando a função type(). 
- Crie uma variável chamada frase que contenha a concatenação das variáveis nome, idade e cidade, formando uma frase como "Alice tem 25 anos e mora em [cidade]". 
'''

import math

cidade = str('São Paulo')
idade = int(18)
pi = float(math.pi)
verdade = bool(True)

print(f'{cidade} - {type(cidade)}')
print(f'{idade} - {type(idade)}')
print(f'{pi} - {type(pi)}')
print(f'{verdade} - {type(verdade)}')

nome = input('\nDigite seu nome: ')
frase = (f'{nome} tem {idade} anos e mora em {cidade}.')
print(frase)
