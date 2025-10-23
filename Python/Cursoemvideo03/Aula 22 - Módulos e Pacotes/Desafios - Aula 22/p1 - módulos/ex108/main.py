# Adapte o código do desafio 107, 
# criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

from moeda import moeda, metade, dobro, aumentar, diminuir


num = float(input('Digite um preço: R$ '))
tax = int(input('Taxa de Aumento/Redução: '))

print(f'A metade de {moeda(num)} é {moeda(metade(num))}')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'Aumentando {tax}%, temos {moeda(aumentar(num, tax))}')
print(f'Diminuindo {tax}%, temos {moeda(diminuir(num, tax))}')
