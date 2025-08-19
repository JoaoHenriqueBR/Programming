'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)

Adicione também as docstrings da função.
'''

def notas(*n, sit=False):
    """
    -> Função para analisar várias notas.
    :param n: Recebe uma ou mais notas.
    :param sit: (OPCIONAL) Indica se deve ou não calcular a situação do aluno (Aprovado/Reprovado).
    :return: dicionário com várias informações com base nas notas.
    """


    boletim = {'Quantidade':len(n),
               'Maior':max(n),
               'Menor':min(n),
               'Média':sum(n)/len(n),
               }
    
    if sit == True:
        if boletim['Média'] >= 6:
            boletim['Situação'] = 'Aprovado'
        else:
            boletim['Situação'] = 'Reprovado'
    
    return boletim


# Programa Principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)

# docstrings
help(notas)
