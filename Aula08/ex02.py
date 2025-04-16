#ex04B.py está mais agil e melhor, chegamos no mesmo resultado

inversa = ''

string = input("Digite um texto: ")

for x in string: # x equivale ao indice da string
    inversa =  x + inversa # o valor de x é adicionado a inversa, que começa vazia, e depois vai se tornando a string invertida

print(inversa)
