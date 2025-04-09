n1 = float(input("Digite a nota: "))
n2 = float(input("Digite a nota dois: "))

media = (n1 + n2) // 2

#A
if media >= 9.0:
    print("Parabéns sua nota foi 'A' você foi aprovado")
#B
elif media >= 7.5 and media < 9.0:
    print("Parabéns sua nota foi 'B' você foi aprovado")

#C
elif media >= 6.0 and media < 7.5:
    print("Parabéns sua nota foi 'C' você foi aprovado")

#D
elif media >= 4.0 and media < 6.0:
    print("Sua nota foi 'D' você foi reprovado")

#E   
elif  media < 4.0:
    print("Sua nota foi 'E' você foi reprovado")
    
else:(print("Notas inválidas"))