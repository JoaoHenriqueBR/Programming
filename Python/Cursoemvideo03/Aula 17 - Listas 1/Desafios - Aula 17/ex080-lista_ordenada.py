# Crie um programa onde o usuário possa digitar cinco valores númericos e
#   cadastre-os em uma lista,
#   já na posição correta de inserção
#   (sem usar o sort()).
#
# No final, mostre a lista ordenada na tela.

numeros = []
for c in range(0, 5):
    n = int(input("Digite um número: "))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista...')
    else:
        for i, num in enumerate(numeros):
            if n <= num:
                numeros.insert(i, n)
                print(f'Adicionado na posição {i} da lista...')
                break
            
        
print("-="*30)
print(f"Lista ordenada: {numeros}")
