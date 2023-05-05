# Faça um programa que leia uma frase e mostre:
#
# - Quantas vezes aparece a letra "A";
# - Em que posição ela aparece pela primeira vez;
# - Em que posição ela aparece pela última vez.
#

frase = input("Digite uma frase: ").strip().lower()


print('A letra A aparece {} vezes!'.format(frase.count('a')))
print('Ela aparece pela 1º vez ma {}ª posição!'.format(frase.find('a') + 1))
print('Ela aparece pela última vez na {}ª posição!'.format(frase.rfind('a') + 1))
