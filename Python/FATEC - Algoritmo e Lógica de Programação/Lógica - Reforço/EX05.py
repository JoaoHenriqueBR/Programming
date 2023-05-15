# Escreva um algoritmo para ler o número total de eleitores de um município,
# o número de votos em branco, nulos e válidos. 
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores
# e emita os resultados.

t = int(input('Quantos eleitores participaram: '))

b = 0
n = 0
valido = 0

for x in range(t):
    print('------ Eleitor {} ------'.format(x+1))
    print('[1] para branco \n[2] para nulo \n[3] para valido ')
    v = int(input('Seu voto:'))
    if v == 1:
        b = b + 1
    elif v == 2:
        n = n + 1
    elif v == 3:
        valido = valido + 1
    else:
        print('Escolha invalida, tente novamente!')
        break

print('Votos BRANCOS: {} votos - {}%'.format(b, 100*b/t))
print('Votos NULOS: {} votos - {}%'.format(n, 100*n/t))
print('Votos VÁLIDOS: {} votos - {}%'.format(valido, 100*valido/t))
