'''
Crie um programa onde o usuário digite uma expressão qualquer que usa parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos ou fechados na ordem correta.
'''

expressao = input("Digite uma expressão matemática: ")
pilha = []

for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")

