# Crie uma função chamada inverte_lista que aceite uma lista como parâmetro
# e retorne uma nova lista com os elementos na ordem inversa.

lista = []
inverso = []

def inverte_lista(lista):
    lista.reverse()
    return lista

while (1):
    x = (input('Acrescente algo na lista (0 para parar): ')).strip()
    if x == '0':
        break
    lista.append(x)

print(lista)
print(inverte_lista(lista))

