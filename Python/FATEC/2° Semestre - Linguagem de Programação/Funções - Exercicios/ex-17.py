# Crie uma função chamada converte_fahrenheit_para_celsius que aceite uma temperatura em Fahrenheit como parâmetro e retorne a temperatura equivalente em graus Celsius. 

def converte_fahrenheit_para_celsius(f):
    c = (f-32)/1.8
    print("Temperatura em Celsius: {}ºC".format(c))

converte_fahrenheit_para_celsius(f=int(input("Temperatura em Fahrenheit: ")))
