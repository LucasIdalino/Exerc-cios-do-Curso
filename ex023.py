n = int(input("Digite um número: "))


u = n // 1 % 10     #Separa unidade
d = n // 10 % 10    #Separa dezena
c = n // 100 % 10   #Separa centena
m = n // 1000 % 10  #Separa milhar

cor = {"azul": "\033[1;34m",
       "vermelho": "\033[1;31m",
       "amarelo": "\033[1;33",
       "verde": "\033[1;32m"}

print("Unidade: ", u)
print("Dezena: ", d)
print("Centena: ", c)
print("Milhar: ", m)
