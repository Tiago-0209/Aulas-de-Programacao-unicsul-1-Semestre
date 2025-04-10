soma = 0.0
resp = 's'
qnt = 0 

while resp == 's'  or resp == 'S':
    num = float(input("Digite um número: "))
    soma = soma + num
    qnt = qnt + 1
    resp = input("Deseja continuar? [s/n] ") 

media = soma / qnt
print(f"A média dos números digitados é: {media}")