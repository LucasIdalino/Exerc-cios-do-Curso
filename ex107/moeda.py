def aumentar(preço, taxa):
    resul = preço + (preço * taxa/100)
    return resul


def diminuir(preço, taxa):
    resul = preço - (preço * taxa/100)
    return resul


def dobro(preço):
    resul = preço * 2
    return resul



def metade(preço):
    resul = preço / 2
    return resul
