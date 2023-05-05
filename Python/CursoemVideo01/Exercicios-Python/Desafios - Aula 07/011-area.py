# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Largura da parede (em metros); '))
h = float(input('Altura da parede (em metros): '))

a = l*h
t = a/2

# Idéia minha, decidi fazer com o que eu sabia do curso de Algoritmos.
if t == 1:
    print('Com uma área de {}m², é necessário {} litro de tinta para pintar esta parede!'.format(a, t))
if a == 0:
    print('Sua parede não existe! ')
else:
    print('Com uma área de {}m², são necessários {} litros de tinta para pintar esta parede!'.format(a, t))
