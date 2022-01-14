def fatorial(n, show=False):
    """
    A função fatorial calcula o fatorial de um número.
    Se utilizar o comando "show=True", a função mostrará o cálculo.
    Se utilizar o comando "show=False", a função não mostrará o cálculo.
    """
    f = 1
    print("=="*15)
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)
