# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

from os import system

c = 1
while c == 1: # loop em caso de erro
    c = 0
    try: # tenta ler um valor
        n = int(input('Digite um número inteiro: '))
    except: # se erro
        system('clear')
        c = 1
        print('Inválido! Precisa ser um número inteiro. ')

if n % 2 != 0 and n % 3 != 0:
    print('Ele é primo!')
elif n == 2 or n == 3:
    print('Ele é primo!')
else:
    print('Não é primo!')
    def div(n): # função para descobrir os divisores
        for c in range(1, n // 2 + 1):  # gerador com os possíveis divisores do número (1 -> Metade inteira + 1)
            if n % c == 0: # Se é divisor
                yield c # Aprendi sobre o yield recentemente: A cada momento em que o "yield" é executado até o fim do loop, ele retorna o valor do c na função
        yield n # Qualquer número é divisivel por ele mesmo (o yield tbm retornará seu valor)
    
    print('Divisível por: {}'.format(list(div(n)))) # Mostra uma lista com os valores do "yield"

