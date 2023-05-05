n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
x = n1*n2
d = n1/n2
dI = n1//n2
e = n1**n2

print('Entre {} e {}: \n A soma é {}, \n O produto é {} \n e a divisão é {:.3f}'.format(n1, n2, s, x, d))
print('Enquanto a divisão inteira é {} \n e a potência é {}'.format(dI, e))
