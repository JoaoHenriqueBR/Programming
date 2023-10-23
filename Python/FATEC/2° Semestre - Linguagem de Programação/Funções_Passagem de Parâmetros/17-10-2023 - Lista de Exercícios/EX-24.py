# Crie uma função chamada calculaMaiorProduto 
# que recebe uma lista  de inteiros como parâmetro e seu tamanho 
# e retorna o maior produto entre quaisquer dois elementos do lista. 



def calculaMaiorProduto(inteiros, tam):
    maior = 0
    for x in inteiros:
        for y in inteiros:
            if x * y >= maior and x != y:
                maior = x * y
    return maior

inteiros = [1, 2, 4, 5, 6, 7, 0, 3]

print(calculaMaiorProduto(inteiros, tam=len(inteiros)))
