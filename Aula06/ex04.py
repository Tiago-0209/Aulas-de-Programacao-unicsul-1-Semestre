import math

Apintada = float(input("Digite o tamanho em metros da área ser pintada: "))

litros = Apintada / 3
lt = litros / 18 
valor = math.ceil(lt * 80)

print(f"Você precisará de {lt} latas de tinta.")
print(f"O valor total a ser pago é R${valor:.2f}")
    


    


    