mais18 = 0
homem = 0
mulhermenos20 = 0
pergunta = " "
while True:
    idade = int(input("Informe a idade: "))
    if idade >= 18:
        mais18 += 1
    sexo = str(input("Informe o sexo: ")).upper().strip()[0]
    while sexo != "M" and sexo != "F":
        sexo = str(input("Informe o sexo: ")).strip().upper()[0]
    if sexo == "M":
        homem += 1
    if sexo in "F" and idade < 20:
        mulhermenos20 += 1
    pergunta = str(input("Deseja continuar? ")).upper().strip()[0]
    while pergunta not in "SN":
        pergunta = str(input("Deseja continuar? ")).upper().strip()[0]
    if pergunta == "N":
        break
print("Fim")
print(f"Temos {mais18} pessoa(s) com mais de 18 anos.")
print(f"Ao todo tem {homem} homem(ns).")
print(f"Ao todo tem {mulhermenos20} mulher(es) com menos de 20 anos.")
