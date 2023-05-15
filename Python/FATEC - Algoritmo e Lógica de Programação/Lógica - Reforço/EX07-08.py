# Cálculo do Peso Ideal. (IMC – índice de massa corpórea)

h = float(input('Digite sua altura (m): '))
s = int(input('Qual seu sexo? (1 - Masculino; 2 - Feminino): '))

if s == 1:
    peso = (72.7*h) - 58
    print('Seu peso ideal é: {:.2f}KG'.format(peso))
elif s == 2:
    peso = (62.1*h) - 44.7
    print('Seu peso ideal é: {:.2f}KG'.format(peso))
else:
    print('Escolha invalida, tente novamente!')
