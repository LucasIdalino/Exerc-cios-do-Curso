from datetime import date
print("+-" * 10, "\033[1;36mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m", "+-" * 10)

ano = int(input("Qual o seu ano de nascimento? "))
idade = date.today().year - ano
print("O(A) atleta tem {} anos.".format(idade))
if idade <= 9:
    print("O(A) atleta é da categoria MIRIM.")
elif idade <= 14:
    print("O(A) atleta é da categoria INFANTIL.")
elif idade <= 19:
    print("O(A) atleta é da categoria JUNIOR.")
elif idade <= 20:
    print("O(A) atleta é da categoria SÊNIOR.")
elif idade > 20:
    print("O(A) atleta é da categoria MASTER.")

