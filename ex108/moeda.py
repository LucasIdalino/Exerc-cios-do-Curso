def aumento(preco=0, taxa=0):
    r = preco + (preco * taxa/100)
    return r


def diminuir(preco=0, taxa=0):
    r = preco - (preco * taxa/100)
    return r


def dobro(preco=0):
    r = preco * 2
    return r


def metade(preco=0):
    r = preco / 2
    return r


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
