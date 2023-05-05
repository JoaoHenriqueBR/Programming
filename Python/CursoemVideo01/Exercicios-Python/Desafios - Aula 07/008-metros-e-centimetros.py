# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Quantos metros são?: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m*10
cm = m*100
mm = m*1000

print('{} metros são: \n {}km \n {}hm \n {}dam'.format(m, km, hm, dam))
print(' {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(dm, cm, mm))
