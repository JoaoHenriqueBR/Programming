# Modifique o programa anterior de forma a ler um numero n. Imprima os n primeiros números primos.

print('Descubra os n primeiros números primos.')
n = int(input('Digite um número: '))

primos = []
p = q = 0

while p < n:
  tot = 0
  q += 1
  for c in range(1, q+1):
    if q % c == 0:
        tot += 1
  if tot == 2:
    p += 1
    primos.append(q)

print(f'Números primos: {primos}')
