#Módulo datetime importando a classe date
from datetime import date
n = int(input("Digite o ano para saber se é bissexto: "))
if n == 0:
    #Class "date." mais método "today().year" que identifica o ano atual.
    n = date.today().year

    #Condição para saber se o ano digitado é bissexto ou não.
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("\033[1;32m{} é um ano bissexto.\033[m".format(n))
else:
    print("\033[1;31m{} não é um ano bissexto.\033[m".format(n))