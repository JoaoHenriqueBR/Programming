a = [2, 3, 4, 7]
b = a[:] # Se b = a, cria uma ligação de uma lista a outra, invés de uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
