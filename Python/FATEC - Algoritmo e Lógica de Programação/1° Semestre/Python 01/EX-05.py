# Desenvolva um programa que entre com a nota de Algorítimo, 
# a nota da disciplina matemática, a de Arduíno e a de Inglês. 
# Efetue a média aritimética do bimestre e mostre na tela. 
# Pergunte ao usuário se deseja calcular outras médias ou encerrar o programa.

r = 1
while r == 1:
    alg = float(input('Digite a nota em Algoritmo: '))
    mat = float(input('Digite a nota em matemática: '))
    ard = float(input('Digite a nota em Arduíno: '))
    ing = float(input('Digite a nota em Inglês: '))
    med = (alg+mat+ard+ing)/4
    print('MÉDIA = {}'.format(med))
    r = int(input('Deseja repetir? Pressione 1: '))
