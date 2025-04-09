salario = float(input("Digite seu salário: "))
vendas = float(input("Digite o valor de suas vendas: "))

comis = vendas * 0.04
total = salario + comis

print(f'O funcionário vai receber de salário final: {total:.2f}')
print(f'O valor das comissões foi R${comis:.2f}')

