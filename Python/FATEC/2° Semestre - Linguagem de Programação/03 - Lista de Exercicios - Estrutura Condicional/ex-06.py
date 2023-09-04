'''
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas. 
'''

dist = int(input('Distância que deseja percorrer (KM): '))

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45

print(f'Preço da passagem será: R$ {preco:.2f}') 
