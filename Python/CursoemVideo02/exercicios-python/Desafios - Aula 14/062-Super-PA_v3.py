# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar alguns termos.
# O programa encerra quando ele dizer que quer mostrar 0 termos.

print('='*15)
print('Super PA')
print('='*15)

termo = int(input('O primeiro termo da PA: '))
r = int(input('A razão da PA: '))
quant = int(input('Quantidade de termos: '))

c = 0
while quant > 0:
    f = termo + (quant-1)*r
    while termo <= f:
        print('{} '.format(termo), end='-> ')
        termo += r
        c += 1
    print('PAUSA! ')
    quant = int(input('Quantos termos quer mostrar a mais?: '))
print(f'Progressão finalizado com {c} termos mostrados.')
