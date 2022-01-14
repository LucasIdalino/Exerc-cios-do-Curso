from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Em que ano você nasceu: "))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} pessoas são maior de idade.")
print(f"{menor} pessoas são menor de idade.")
