# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda


num = float(input('Digite um preço: R$ '))
tax = int(input('Taxa de Aumento/Redução: '))

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, False)}')
print(f'Aumentando {tax}%, temos {moeda.aumentar(num, tax, True)}')
print(f'Diminuindo {tax}%, temos {moeda.diminuir(num, tax, True)}')
