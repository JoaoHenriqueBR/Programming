# Escreva um programa que mostre os números de 1 até um numero digitado pelo usuário, mas, apenas os números impares. 

print("~="*20)
print('CONTAGEM DE NÚMEROS IMPARES')
print("~="*20)

f = int(input('Digite o número final da contagem: '))

for n in range(1, f+1, 2):
  print(n)
  