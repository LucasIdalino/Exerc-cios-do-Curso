def aumento(preco=0, taxa=0, formato=False):
    """
    A função aumentar, aumenta um valor ao definir uma porcentagem.

    preço: parâmetro valor de entrada.
    taxa: parâmetro porcentagem de entrada.
    formato: False ou True para mostrar ou não o valor convertido em R$
    """
    r = preco + (preco * taxa/100)
    return r if formato is False else moeda(r)


def diminuir(preco=0, taxa=0, formato=False):
    r = preco - (preco * taxa/100)
    return r if formato is False else moeda(r)


def dobro(preco=0, formato=False):
    r = preco * 2
    return r if formato is False else moeda(r)


def metade(preco=0, formato=False):
    r = preco / 2
    return r if formato is False else moeda(r)


def moeda(preco=0, coin="R$"):
    return f'{coin}{preco:.2f}'.replace('.', ',')
