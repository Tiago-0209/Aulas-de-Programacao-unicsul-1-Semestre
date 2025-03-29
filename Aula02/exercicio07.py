print("conversor de celcius em kelvin e fahrenheit!")
tc = float(input("digite o valor da temperatura em celcius: "))

tf = 1.8 * tc + 32

tk = tc + 273

print(f"o valor de {tc}°C em kelvin é de {tk:.2f}°K")
print(f"o valor de {tc}°C em fahrenheit é de {tf:.2f}°F")