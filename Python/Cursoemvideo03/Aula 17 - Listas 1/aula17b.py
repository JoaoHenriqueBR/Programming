valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na poição {c} encontrei o valor {v}!')
print('Cheguei na final da lista.')

