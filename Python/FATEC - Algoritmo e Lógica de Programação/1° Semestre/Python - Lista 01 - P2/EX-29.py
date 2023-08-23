'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

11. Atleta: Rodrigo Curvêllo

12.

13. Primeiro Salto: 6.5 m

14. Segundo Salto: 6.1 m

15. Terceiro Salto: 6.2 m

16. Quarto Salto: 5.4 m

17. Quinto Salto: 5.3 m

18.

19. Melhor salto: 6.5 m

20. Pior salto: 5.3 m

21. Média dos demais saltos: 5.9 m

22.

23. Resultado final:

Rodrigo Curvêllo: 5.9 m
'''

from math import inf

ordem = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
atletas = []

melhor = contagem = total = media = 0 # Declara as variáveis em uma única linha
pior = inf

atleta = ' '
while atleta != '':
    atleta = input('Nome do Atleta: ').strip()
    if atleta == '':
        break
    atleta_media = parcial = atleta_melhor = 0
    atleta_pior = inf
    for c in range(5):
        salto = 0
        while salto <= 0:
            try:
                salto = float(input(f"{ordem[c]} salto: "))
            except:
                salto = -1
            if salto >= 1:
                break
            else:
                print('Valor inválido! Tente novamente.')
        parcial += salto
        total += salto
        contagem += 1
        if salto > melhor:
            melhor = salto
        if salto < pior:
            pior = salto
        if salto > atleta_melhor:
            atleta_melhor = salto
        if salto < atleta_pior:
            atleta_pior = salto
    atleta_media = (parcial - (atleta_melhor + atleta_pior)) / 3
    media = (total - (melhor + pior)) / (contagem-2)
    atletas.append(atleta)
    atletas.append(atleta_media)

print('{} Resultado GERAL {}'.format("="*10, "="*10))
print(f"Melhor salto: {melhor} m")
print(f"Pior salto: {pior} m")
print(f"Media dos demais saltos: {media:.2f} m")
print("\n")
print('{} Resultado Final {}'.format("="*10, "="*10))
for c in range(0, len(atletas), 2):
    print(f"{atletas[c]}: {atletas[c+1]:.1f} m")

