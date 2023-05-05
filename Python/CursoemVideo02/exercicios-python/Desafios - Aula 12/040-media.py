# Crie um programa que leia duas notas de um aluno e calcule a média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('~='*10)
print('MÉDIA ESCOLAR')
print('~='*10)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda: '))
media = (n1+n2)/2

if media < 5:
    print('\033[31mREPROVADO!\033[m')
    print('A média foi \033[31m{:.1f}!\033[m'.format(media))
elif media >= 7:
    print('\033[34mAPROVADO!\033[m')
    print('A média foi \033[34m{:.1f}!\033[m'.format(media))
else:
    print('\033[33mRECUPERAÇÃO!\033[m')
    print('A média foi \033[33m{:.1f}!\033[m'.format(media))
