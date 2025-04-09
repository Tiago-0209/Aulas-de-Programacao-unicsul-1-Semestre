segundos_totais = int(input("Digite os segundos: "))

horas = segundos_totais // 3600 
resto = segundos_totais % 3600
minutos = resto // 60  
segundos = resto % 60

print(f'O valor será ||Horas: {horas}||Minutos: {minutos}||Segundos: {segundos}')
