'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 

No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoas = list()
dados = dict()
total = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Digite o seu nome: '))
    
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    
    dados['idade'] = int(input('Idade: '))
    total += dados['idade']

    pessoas.append(dados.copy())

    while True:
        r = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if r == 'N':
        break


quant_pessoas = len(pessoas)
media = total / quant_pessoas

print('-='*30)

print(f'A) Ao todo tempos {quant_pessoas} cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')

for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()

print('D) Lista das pessoas que estão acima da média: ')

for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')

