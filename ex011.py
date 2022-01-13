alt = float(input("\033[1;33mQual a altura da parede?\033[m: "))
lar = float(input("\033[1;33mQual a largura da parede?\033[m: "))

#Calcula o metro quadrado
area = alt*lar
t = area/2.0


#Dimensões da parede
print("Sua parede tem \033[1;34m{}\033[m x \033[1;34m{}\033[m".format(alt, lar))

#Quantidade em litros
print("Você precisará de {:.1f}l de tinta para pintar sua sala de \033[1;35m{:.2f}\033[mm²".format(t, area))
