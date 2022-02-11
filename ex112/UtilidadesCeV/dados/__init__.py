def leiadinheiro(msg):
    validade = False
    while not validade:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == "":
            print(f'Erro! {entrada} não é um preço válido')
        else:
            validade = True
            return float(entrada)


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Por favor, digite um número inteiro.")
        if ok:
            break
    return valor


