#Dissecando uma variável.
n = input("\033[1;34;40mQuém é você?\033[m:")

#Tipo da variável.
print("O tipo primitivo desse valor é:", type(n))

#Se o valor da variável é alfabética.
print("\033[1;30mÉ letra?\033[m:", n.isalpha())

#Se o valor da variável é numérica.
print("\033[1;31mÉ número?\033[m:", n.isnumeric())

#Se o valor da variável é MAIÚSCULA.
print("\033[1;32mTem letra maiúscula?\033[m:", n.isupper())

#Se é minúscula.
print("\033[1;33mTem letra minúscula?\033[m:", n.islower())

#Se é alfanumérico.
print("\033[1;34mÉ alfanúmerico?\033[m:", n.isalnum())

#Se é capitalizado.
print("\033[1;35mEstá capitalizada?\033[m:", n.istitle())

print("\033[1;36;40mMuito obrigado!\033[m")
