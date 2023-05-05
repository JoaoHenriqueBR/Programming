# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Insira uma nota: '))
n2 = float(input('Insira outra: '))
m = (n1+n2)/2

print('A média do aluno foi {:.1f}'.format(m))
