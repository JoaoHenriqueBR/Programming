# Escreva um programa que mostre os números de 1 até o numero digitado pelo usuário, mas, apenas os números múltiplos de 3. 

print("~="*20)
print('CONTAGEM DE MÚLTIPLOS DE 3')
print("~="*20)

f = int(input('Digite o número final da contagem: '))

for n in range(3, f+1, 3):
  print(n)
