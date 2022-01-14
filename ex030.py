n = int(input("\033[1;33mDigite um número\033[m: "))
resultado = n % 2
if resultado == 0:
    print("\033[1;31mO número {} é par.\033[m".format(n))
else:
    print("\033[1;32mO número {} é ímpar\033[m".format(n))
