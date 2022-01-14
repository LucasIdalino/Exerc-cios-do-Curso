frase = str(input("\033[1;32mFrase\033[m: ")).upper().lower().strip()

#A função .count(), conta quantas letras dentro do parâmetro aplicado existem dentro do valor da variável.
print("A letra aparece:", frase.count("a"))

#A função .find() busca a primeira letra dentro do parâmetro aplicado no valor da váriavel.
print("Aparece pela primeira vez na posição:", frase.find("a"))

#A função .rfind() busca a última letra dentro do parâmetro aplicado no valor da váriavel.
print("Aparece pela última vez:", frase.rfind("a"))
