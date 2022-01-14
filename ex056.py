homemvelho = 0
mulhermenos20 = 0
somaidade = 0
for c in range(1, 7):
    print(("*=" * 10), "{}º pessoa".format(c), ("*="*10))
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    somaidade += idade
    if sexo in "Mm" and idade > homemvelho:
        homemvelho = idade
    if sexo in "Ff" and idade < 20:
        mulhermenos20 += 1
média = somaidade/6
print(f"A média de idade de todos é {média:.2f}.")
print(f"O homem mais velho tem {homemvelho} anos.")
print(f"{mulhermenos20} mulhere(s) tem menos de 20 anos")
