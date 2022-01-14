saque = int(input("Quanto você que sacar? "))
total = saque
totcéd = 0
céd = 50
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f"Total de {totcéd} cédeulas de R${céd}.")
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
