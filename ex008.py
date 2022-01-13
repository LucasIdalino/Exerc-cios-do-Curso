m = float(input("Quantos metros?:"))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cent = m*100
mili = m*1000

#Conversor de medidas. Km, Hm, Dam, Dm, Cent, Mili.

print("\033[1;31m{}\033[m metros(s) tem \033[1;32m{}\033[m quilometros".format(m, km))
print("\033[1;31m{}\033[m metro(s) tem \033[1;32m{}\033[m hectometros".format(m, hm))
print("\033[1;31m{}\033[m metros(s) tem \033[1;32m{:.2f}\033[m dametros".format(m,dam))
print("\033[1;31m{}\033[m metro(s) tem \033[1;32m{:.0f}\033[m decimetro".format(m, dm))
print("\033[1;31m{}\033[m metro(s) tem \033[1;32m{:.0f}\033[m centímetros.".format(m, cent))
print("\033[1;31m{}\033[m metro(s) tem \033[1;32m{:.0f}\033[m milímetros.".format(m, mili))


print("Obrigado!")