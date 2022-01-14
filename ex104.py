def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;31mErro! Digite um número.\033[m")
        if ok:
            break
    return valor


n = leiaint("Digite um valor: ")
print(f"Você digitou o valor {n}.")
