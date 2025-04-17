texto = input("Digite um texto: ")
pontuacao = ["." , "," , ":" , ";" , "!" , "?"]

#remover os sinais de pontuação

for p in pontuacao:
    texto = texto.replace(p, "")

    #split para devolver uma lista com as palavras como otedi
print(texto.split)
lista = texto.split()
numero_Palavras = len(lista)
print("O número de palavras é: ", numero_Palavras)
#len para contar o número de palavras na lista
print(lista)