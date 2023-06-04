# Faça um programa que leia e valide as seguintes informações:
#
# 1. Nome: maior que 3 caracteres;
#
# 2. Idade: entre 0 e 150;
#
# 3. Salário: maior que zero;
#
# 4. Sexo: 'f' ou 'm';
#
# 5. Estado Civil: 's', 'c', 'v', 'd';

from os import system

nome = input('Digite seu nome: ').strip()

while len(nome) <= 3:
    print('Nome Inválido! Precisa ter 3 ou mais caracteres!')
    nome = input('Digite novamente seu nome: ')
else:
    system('clear')
    print('Nome válido! \n')

try:
    id = int(input('Quantos anos você tem: '))
except:
    id = 0

while id <= 0 or id >= 150:
    print('Idade Inválida! Precisa ser entre 0 e 150 anos')
    try:
        id = int(input('Digite novamente sua idade: '))
    except:
        id = 0
else:
    system('clear')
    print('Idade válida! \n')

try:
    sal = float(input('Seu salário: R$ '))
except:
    sal = 0

while sal <= 0:
    print('Salário Inválido! Precisa ser maior que R$ 0')
    try:
        sal = float(input('Informe seu salário novamente: R$ '))
    except:
        sal = 0
else:
    system('clear')
    print('Salário válido! \n')

sex = input('Seu sexo (f -> Feminino; m -> masculino): ').strip().upper()

while sex != 'F' and sex != 'M':
    print('Sexo inválido! (f -> Feminino); (m -> Masculino) - Sexo biológico')
    sex = input('Digite novamente seu sexo: ').upper()
else:
    system('clear')
    print('Sexo válido! \n')
    
civil = input('Por último, o seu estado civil (s -> solteiro(a); c -> casado(a); v -> viúvo(a); d -> divorciado): ').lower().strip()

estados = ['s', 'c', 'v', 'd']
while civil not in estados:
    print('Estado cívil inválido! Precisa ser entre: (s -> solteiro(a); c -> casado(a); v -> viúvo(a); d -> divorciado)')
    civil = input('Tente novamente: ').lower().strip()
else:
    system('clear')
    print('Todos os dados foram válidados com sucesso! \n')

print('SEUS DADOS \n')
print(f'Nome: {nome}.')
print(f'idade: {id} Anos.')
print('Salário: R$ {:.2f}'.format(sal))
print(f'Sexo: {sex}')
print(f'Estado Cívil: {civil}')
