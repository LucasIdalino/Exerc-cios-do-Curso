print("Índice de Massa Corporal")

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))

imc = peso / (altura ** 2)

print("{:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal")
elif 25 < imc <= 30:
    print("Você está no sobrepeso.")
elif imc > 30 and imc <= 40:
    print("Você tem obesidade.")
elif imc > 40:
    print("Você tem obesidade morbida.")
