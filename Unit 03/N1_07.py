##N1_07 Maior e Menor: Peça dois números e mostre qual deles é o maior ou se são iguais.

number_a = int(input("Digite um numero [X]: "))
number_b = int(input("Digite um outro numero [Y]: "))

if number_a == number_b:
    print(f"Ambos numeros X e Y são iguais valor [{number_a}]")
elif number_a > number_b:
    print(f"Primeiro numero X é maior que numero Y ou seja : {number_a} > {number_b}")
else:
    print(f"Segundo numero Y é maior que numero X ou seja : {number_b} > {number_a}")

