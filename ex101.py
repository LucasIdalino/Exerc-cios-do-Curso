def voto(ano):
    from datetime import datetime

    idade = datetime.now().year - ano

    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif idade >= 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        if idade >= 16:
            return f"Com {idade} anos: VOTO OBRIGATÓRIO."


a = int(input("Ano de Nascimento: "))
print(voto(a))
