c = int(input("\033[1;31mInforme a temperatura em °C\033[m: "))

#Conversor de Temperatura de °C para °F
f = ((9 * c) / 5) + 32
print("A temperatura de \033[1;34m{}°C\033[m, correspende a \033[1;33m{}°F.\033[m".format(c,f))
