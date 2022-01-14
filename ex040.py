print("MÉDIA DO SEMESTRE")

n1 = float(input("Sua primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

média = (n1 + n2 + n3) / 3
print("Sua média foi {:.2f}".format(média))

if média < 5.0:
    print("\033[1;31mVocê não foi aprovado.\033[m")
    print("Não desista, seja persistente e estude.")
elif média == 5.0 or média <= 6.9:
    print("\033[1;33mVocê está na recuperação.\033[m")
    print("Não se lamente, você chegou bem perto, ainda é possível você se recuperar.")
elif média >= 7.0:
    print("\033[1;32mVocê foi aprovado.\033[m")
    print("Parabéns! Sempre dê o seu melhor!")
