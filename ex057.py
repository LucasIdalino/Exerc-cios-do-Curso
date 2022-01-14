sexo = str(input("Qual o seu sexo? ")).strip().upper()[0]

#Estrutura de repetição (loop) while.
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).upper().strip()[0]
print("Sexo {} registrado com sucesso.".format(sexo))
