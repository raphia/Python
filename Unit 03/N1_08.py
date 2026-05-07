##Par ou Ímpar: Crie um programa que receba um número e diga se ele é par ou ímpar usando o operador % [even , odd]

number = int(input("Digite um numero inteiro: "))

if number == 0: 
    print("Neutro")
elif (number%2) == 0:
    print("Par")
else:
    print("Impar")