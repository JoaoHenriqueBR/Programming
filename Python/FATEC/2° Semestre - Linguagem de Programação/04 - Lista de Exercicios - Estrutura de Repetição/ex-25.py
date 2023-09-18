'''
Escreva um programa que calcule a raiz quadrada de um número. 
Utilize o método de Newton para obter um resultado aproximado. 
Sendo n o numero a obter a raizquadrada, considera a base b=2. 
Calcule p usando a formula p=(b+(n/b))/2. 
Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a formula apresentada. 
Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,001. 
'''


n = int(input('Digite um número: '))

b = 2
while (1):
    p = (b + (n / b)) / 2
    quad = p**2
    if quad - n < 0.001:
        break
    b = p

print(f'Raiz Quadrada de {n} = {p}')

