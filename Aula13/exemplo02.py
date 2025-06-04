def calcularIMC(argpeso, argaltura):
   imc = argpeso / (argaltura ** 2)
   print(f"o imc é {imc}")
   return(imc)

   
def classificarIMC(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("peso ideal")
    else:
        print("Sobrepeso")

def entradadados():
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    ret = calcularIMC(peso, altura)
    classificarIMC(ret)

entradadados()
