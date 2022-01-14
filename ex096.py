#As funções "def...(), são funções programadas para executar comandos. As funções em python podem ser criadas pelo programador/desenvolvedor."
def medidas(l, c):
    metroquadrado = (l*c)
    print(f"A área de um terreno de {l}x{c} é de {metroquadrado}m².")


print("Controle de Terreno")
print("=-"*20)
medidas(l=(float(input("Largura (m): "))), c=(float(input("Comprimento (m): "))))
