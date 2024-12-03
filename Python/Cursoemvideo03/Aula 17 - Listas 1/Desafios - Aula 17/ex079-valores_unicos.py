# Crie uma programa onde o usuário possa digitar vários valores númericos e
#   cadastre-os em uma lista.
# Caso o número já exista lá dentro,
#   ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados,
#   em ordem crescente.

valores = []
while True:
    n = int(input("Digite um número: "))
    if n in valores:
        print("Valor já na lista.")
    else:
        valores.append(n)
        print("Valor adicionado com sucesso!")
    r = input("Deseja continuar? (s/n): ")
    if r in 'Nn':
        break

print(f"Foi digitado os valores {sorted(valores)}.")
