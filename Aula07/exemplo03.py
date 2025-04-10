'''
contador = 1
while contador <= 10:
    nota1 = float(input(f"Digite a primeira nota: "))
    nota2 = float(input(f"Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média do aluno {contador} é: {media}")
    contador = contador + 1
'''

for i in range(1, 11):
    nota1 = float(input(f"Digite a primeira nota: "))
    nota2 = float(input(f"Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média do aluno {i} é: {media}")

    '''
    podemos usar o for para fazer a mesma coisa que o while, mas o for é mais utilizado quando sabemos quantas vezes queremos repetir um bloco de código.
    O while é mais utilizado quando não sabemos quantas vezes queremos repetir um bloco de código.
    '''
