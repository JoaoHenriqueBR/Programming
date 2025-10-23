'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas

aumentar()
diminuir()
dobro()
metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

num = int(input('Digite um preço: R$ '))
tax = int(input('Taxa de Aumento/Redução: '))

print(f'A metade de R$ {num:.2f} é R$ {moeda.metade(num):.2f}')
print(f'O dobro de R$ {num:.2f} é R$ {moeda.dobro(num):.2f}')
print(f'Aumentando {tax}%, temos R$ {moeda.aumentar(num, tax):.2f}')
print(f'Diminuindo {tax}%, temos R$ {moeda.diminuir(num, tax):.2f}')
