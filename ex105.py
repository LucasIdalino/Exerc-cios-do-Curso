def notas(*n, sit=False):
    aluno = dict()
    aluno["notas"] = len(n)
    aluno["maior"] = max(n)
    aluno["menor"] = min(n)
    aluno["média"] = sum(n)/len(n)
    if sit:
        if aluno["média"] >= 7:
            aluno["situação"] = "Boa"
        elif aluno["média"] >= 5:
            aluno["situação"] = "Razoável"
        else:
            aluno["situação"] = "Ruim"
    return aluno


resp = notas(7, 8, 9, sit=True)
print(resp)
