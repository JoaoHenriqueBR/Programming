#  Crie uma função chamada calculaFibonacci que recebe um número inteiro positivo como parâmetro
#  e retorna o número na sequência de Fibonacci correspondente à posição dada. 

def calculaFribonacci(n):
    lista = [0, 1] 
    cont = 0
    x = 0
    y = 1
    while cont != n - 2:
        f = x+y
        x = y
        y = f
        lista.append(f)
        cont +=1
    return lista 

print(calculaFribonacci(n=int(input("Digite um número: "))))
