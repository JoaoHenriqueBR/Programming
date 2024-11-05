print('Lista: ')
num = [2, 5, 9, 1]
print(num)

print('\nAltera o valor: ')
num[2] = 3
print(num)

print('\nAdiciona um valor: ')
num.append(7)
print(num)

print('\nOrdena os valores: ')
num.sort(reverse=True)
print(num)

print('\nInsere um valor na posição especificada: ')
num.insert(2, 2)
print(num)

#print('\nRemove um elemento pelo indice (O último se nada for especificado): ')
#num.pop(2)
#print(num)

print('\nRemove o primeiro elemento com o valor mencionado: ')
num.remove(2)
print(num)

# Condicional
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')



print(f'\nEssa lista tem {len(num)} elementos.')
