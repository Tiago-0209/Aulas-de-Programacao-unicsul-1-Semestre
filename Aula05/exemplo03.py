n1 = float(input("digite um numero: "))
n2 = float(input("digite um outro numero: "))
n3 = float(input("digite mais um numero: "))

if n1>n2 and n1>n3:
    print(f" {n1} é o maior numero dentro os digitados")
elif n2 > n1 and n2>n3:
    print(f" {n2} é o maior numero dentro os digitados")
else:
    print(f" {n3} é o maior numero dentro os digitados")