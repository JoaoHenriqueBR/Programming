'''
Escreva um programa que corrija um teste de múltiplas escolhas de três questões. A resposta da primeira questão a resposta é “b”; da segunda, “a”; e da terceira, “d”. O programa conta um ponto a cada resposta correta. Considere a possibilidade do programa aceitar respostas com letra maiúsculas e minúsculas em todas as questões
'''

gabarito = ['B', 'A', 'D']

ponto = 0
for c in range(3):
  questao = input(f'Resposta da {c+1}º questão: ').strip().upper()
  if questao == gabarito[c]:
    print('Resposta CORRETA!')
    ponto += 1
  else:
    print('INCORRETO! ')

print(f'Pontuação: {ponto}/3')
