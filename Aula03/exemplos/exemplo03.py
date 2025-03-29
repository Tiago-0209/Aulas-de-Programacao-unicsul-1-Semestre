import math
raio = float(input("Digite o raio da circunferência em cm: "))
comprimento = 2 * math.pi * raio
area = math.pi * raio * raio

print(f"o comprimento da circunferência é igual a {comprimento:.2f} cm²")
print("A área da circunferência é igual a %.2f cm²" % (area))