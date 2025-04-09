sex = input("Digite seu sexo: [M] e [F]: ").upper
altura = float(input("Digite sua altura em metros [exemplo: 1.70]: "))


if sex == 'M':
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso:.2f}')
else: 
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso:.2f}')
    

