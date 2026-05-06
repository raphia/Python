#N1_02 Dobro e Triplo: Peça um número e exiba o seu dobro e a sua terça parte.

number = float(input("Digite um numero: "))

double = number * 2 
triple = number * 3
thirth_part = number / 3

## Pela a questão ter ficado ambiguia para evitar erros exiba logo triplo e a terça parte evitando de cara  a falta de informação

print(f"Dobro: {double:.2f}")
print(f"Triplo: {triple:.2f}")
print(f"Terça Parte: {thirth_part:.2f}")