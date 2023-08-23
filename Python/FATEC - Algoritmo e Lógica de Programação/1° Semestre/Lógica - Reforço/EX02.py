import turtle
from time import sleep

# Cria uma lista com opção de cores
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m'}

# Título
print("="*20)
print("Área de um quadrado")
print("="*20)

#  Explica sobre o calculo a ser feito e pergunta o perimetro ao usuário
print("\n{}ÁREA{} = {}Perimetro ^ 2{}".format(
    cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
p = int(input('Digite o perimetro: '))
a = p ** 2
t = turtle.Turtle()

# Uso o turtle para desenhar o quadrado com base no perimetro
for _ in range(4):
    t.forward(p)
    t.left(90)

sleep(5) # Pausa para o usuário admirar o quadrado feito :)

# No final mostro a área do quadrado
print("{}ÁREA:{} {}".format(cores['amarelo'], cores['limpa'], a))
