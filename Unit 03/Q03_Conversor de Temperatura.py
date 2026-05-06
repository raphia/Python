#Peça uma temperatura em Celsius e converta para Fahrenheit usando a fórmula: F = C * 1.8 + 32.

temperature = float(input("Digite a temperatura em Celsius: "))
fahrenheit = temperature * 1.8 + 32
print(f"A temperatura de {temperature}C é equivalente a {fahrenheit:.2f}F")