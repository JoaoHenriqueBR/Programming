'''# Ler o nome de uma pessoa e decidi se ela é foda ou corno com base no nome.

nome = str(input('Qual é o seu nome? '))

if nome == 'João':
    print('Você é foda! ')
else:
    print('Você é corno! ')
print('Seja bem vindo {}!'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('Sua média foi {:.1f}!'.format(m))
if m >= 7.0:
    print('Você foi ótimo! PARABÉNS!')
else:
    print('Você é fraco, lhe falta estudo!')
