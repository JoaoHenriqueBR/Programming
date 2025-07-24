'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''

# Escopo Global
from datetime import date

atual = date.today().year

# Função para calcular capacidade de votar
def voto(ano):
    if atual - ano >= 70:
        voto = "VOTO OPCIONAL."
    else:
        if atual - ano >= 18:
            voto = "VOTO OBRIGATÓRIO!"
        elif atual - ano < 16:
            voto = "Não vota!"
        else:
            voto = "VOTO OPCIONAL."
    
    return voto


# Programa Principal
nasc = int(input("Ano de Nascimento: "))
print(f"Com {atual - nasc} anos: {voto(nasc)}")
