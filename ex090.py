#Váriavel composta do tipo dicionário. dict()
aluno = dict()
aluno["aluno"] = str(input("Aluno(a): ").upper())
aluno["media"] = float(input("Média: "))
if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif 7 > aluno["media"] >= 5:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"
for k, v in aluno.items():
    print(f"{k} é igual {v}.")
