'''
Desafio 1 - João Henrique Alves Ferreira, 2º Semestre - ADS (Manhã) - Fatec Zona Sul

Seu primeiro desafio é criar uma agenda telefônica simples usando um dicionário.
O programa deve solicitar ao usuário o nome do contato e seu número de telefone,
e em seguida, armazenar essas informações no dicionário. 
O usuário pode adicionar quantos contatos desejar. 
Ao final, o programa deve exibir a lista completa de contatos.
'''

c = int(input('Quantos contatos deseja ter na agenda: '))
agenda = {}
i = 0

while i < c:
    if agenda == {}:
        print('\nA agenda telefônica está vazia.')
    nome = str(input('\nDigite o nome do contato: '))
    numero = int(input('Digite o número de telefone: '))
    agenda[nome] = numero
    print('\nContato adicionado com sucesso!')
    i += 1

print('\nContatos na agenda telefônica: ')
for nome, numero in agenda.items():
    print(f'- {nome}: {numero}')

