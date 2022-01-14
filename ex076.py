compras = ("Caderno", 78, "Lápis", 3, "Borracha", 2, "Caneta", 5, "Bolsa", 100)
print("=="*10)
print("Listagem de Preço")
print("=="*10)
for pos in range(0, len(compras)):
    if pos % 2 == 0:
        print(f"{compras[pos]:.<30}", end=" ")
    else:
        print(f"R${compras[pos]:>7.2f}")
