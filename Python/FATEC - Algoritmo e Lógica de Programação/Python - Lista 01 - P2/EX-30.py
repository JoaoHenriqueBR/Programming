'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação
e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

25. Atleta: Aparecido Parente

26. Nota: 9.9

27. Nota: 7.5

28. Nota: 9.5

29. Nota: 8.5

30. Nota: 9.0

31. Nota: 8.5

32. Nota: 9.7

33.

34. Resultado final:

35. Atleta: Aparecido Parente

36. Melhor nota: 9.9

37. Pior nota: 7.5

Média: 9,04
'''

from math import inf

atleta = input('Atleta: ')

total = melhor = 0
pior = inf
for c in range(7):
    nota = 0
    while nota <= 0:
        try:
            nota = float(input("Nota: "))
        except:
            nota = -1
        if nota >= 0:
            break
        else:
            print('Nota inválida! Tente novamente.')
    total += nota
    if nota > melhor:
        melhor = nota
    if nota < pior:
        pior = nota

media = (total - (melhor + pior)) / (c-1)

print('\n')
print('Resultado Final:')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {melhor}')
print(f'Pior nota: {pior}')
print(f'Média: {media}')
