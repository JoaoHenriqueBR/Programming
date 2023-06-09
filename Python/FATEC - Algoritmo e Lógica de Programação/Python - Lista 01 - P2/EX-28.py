'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova 
e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

a. Maior e Menor Acerto;

b. Total de Alunos que utilizaram o sistema;

c. A Média das Notas da Turma.

d. Gabarito da Prova:

e.

f. 01 - A

g. 02 - B

h. 03 - C

i. 04 - D

j. 05 - E

k. 06 - E

l. 07 - D

m. 08 - C

n. 09 - B

10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

from math import inf

resp = 1
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

while resp != 0:
    print('Gabarito: ')
    print(gabarito)
    try:
        resp = int(input('(Diferente de 0 - Alterar; 0 - Manter): '))
    except:
        pass
    if resp == 0:
        break
    quest = int(input('Qual questão deseja mudar (1-10): '))
    alt = input(f'Alternativa {gabarito[quest-1]} -> Para qual deseja mudar: ')
    gabarito[quest-1] = alt



aluno = 1
maior = 0
menor = inf
total = 0

while aluno != 0:
    print('{} ALUNO {} {}'.format('-'*10, aluno, '-'*10))
    nota = 0
    for c in range(10):
        r = ''
        while r not in gabarito:
            r = (input(f'Resposta do Aluno - Questão {c+1}: ')).upper().strip()
            if r in gabarito:
                break
            print('Resposta Inválida! Tente novamente.')
        if gabarito[c] == r:
            nota += 1
    print(f'Nota do Aluno: {nota}\n')
    total += nota
    if nota > maior:
        maior = nota
        n_maior = aluno
    if nota < menor:
        menor = nota
        n_menor = aluno
    try:
        cont = int(input('Outro aluno irá utilizar o sistema? (0 - Encerrar / Diferente de 0 - Continuar): '))
    except:
        cont = 1
        pass
    if cont == 0:
        break
    else:
        aluno += 1

print(f'Maior quantidade de acertos: Aluno {n_maior} - {maior} acertos.')
print(f'Menor quantidade de acertos: Aluno {n_menor} - {menor} acertos.')
print(f'Média: {total/aluno} acertos.')
print('')
print('Gabarito: ')
print(gabarito)

