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


def moeda(preco=0, moedas="R$"):
    return f'{moedas}{preco:.2f}'.replace('.', ',')


def resumo(preco, taxa, taxar):
    print("=="*15)
    print('Resumo do Valor'.center(30))
    print("=="*15)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com aumento de {taxa}%: \t{aumento(preco, taxa, True)}')
    print(f'Com redução de {taxar}%: \t{diminuir(preco, taxar, True)}')
    print("=="*15)

