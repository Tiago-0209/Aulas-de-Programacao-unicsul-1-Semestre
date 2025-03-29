print("calcule a gorjeta do garçom!")
cliente = input("digite o nome do cliente: ")
conta = float(input(f"digite o valor da conta do cliente {cliente}: "))
gorjeta = conta * (10/100)
total = conta + gorjeta

print (f"o valor de gorjeta a ser pago é de R${gorjeta:.2f}")
print (f"o valor de total a ser pago é de R${total:.2f}")