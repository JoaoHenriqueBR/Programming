t = int(input("Entre com uma temperatura: "))
escolha = int(input(" [1] Celsius \n [2] Fahreheint \n [3] Kelvin \n Tipo: "))
converte = int(input("Para qual deseja converter?: "))

if escolha == 1:
    if converte == 2:
        F = 32 + (t * 9 / 5)
        print("Temperatura: {}ºF".format(F))
    elif converte == 3:
        K = t + 273.15
        print("Temperatura: {}ºK".format(K))
    else:
        print("Temperatura: {}ºC".format(t))
elif escolha == 2:
    if converte == 1:
        c = (t-32)/1.8
        print("Temperatura: {}ºC".format(c))
    elif converte == 3:
        K = (t-32) * 5 / 9 + 273
        print("Temperatura: {}ºK".format(K))
    else:
        print("Temperatura: {}ºF".format(t))
elif escolha == 3:
    if converte == 1:
        c = t - 273
        print("Temperatura: {}ºC".format(c))
    elif converte == 2:
        F = (t - 273) * 1.8 + 32
        print("Temperatura: {}ºF".format(F))
    else:
        print("Temperatura: {}ºK".format(t))
else:
    print("Valor invalido! Tente novamente.")    
