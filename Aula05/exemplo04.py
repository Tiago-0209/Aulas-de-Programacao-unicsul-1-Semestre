peso = float(input("digite o seu peso: "))
altura = float(input("digite sua altura: "))
imc= peso / (altura*altura)

if imc <20:
    print("você esta abaixo do peso")
elif imc <25:
    print("você esta no peso normal")
elif imc <30:
    print("Você está em sobrepeso")
elif imc <40:
    print("Você está obeso")
else:
    print("Você está em obesidade morbida")
