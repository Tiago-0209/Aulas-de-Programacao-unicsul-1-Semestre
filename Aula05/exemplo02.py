quarto = input("digite o tipo de quarto: (S,D ou T) ")
diaria = int(input("digite quantos dias ira ficar: "))

if quarto == "S" or quarto == "s":
    total = diaria*255.50
    print(f"o valor total a ser pago é igual a R${total} ")
    
elif quarto == "D" or quarto == "d":
    print(f"o valor total a ser pago é igual a R${diaria*305.50}")
    
elif quarto == "T" or quarto ==  "t":
    print(f"o valor total a ser pago é igual a R${diaria*360.5}")

else:
    print("tipo de quarto invalido")