salario = float(input("\033[1;31mQual o teu salário?\033[m: "))

#Reajuste salarial
aumento = salario + (salario*15/100)
print("Seu novo salário é de \033[1;33m{:.2f}\033[mR$ com 15% de aumento.".format(aumento))
