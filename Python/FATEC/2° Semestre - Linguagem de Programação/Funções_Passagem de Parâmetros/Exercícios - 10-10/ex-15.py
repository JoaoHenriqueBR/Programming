#  Crie uma função chamada calculaFibonacci que recebe um número inteiro positivo como parâmetro
#  e retorna o número na sequência de Fibonacci correspondente à posição dada. 

def calculaFibonacci(n):
    if n <= 0:
        return "O número deve ser maior que 0."
    elif n == 1:
        return 0
    else:
        return (n-1) + (n-2)

print(calculaFibonacci(7))
