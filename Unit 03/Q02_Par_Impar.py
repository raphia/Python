#Par ou Ímpar: Peça um número 
#ao usuário e use o operador % (resto da divisão) 
#para dizer se o número é par ou ímpar. (Dica: se o resto da divisão por 2 for 0, é par).

number = int(input("Digite um numero inteiro: "))
if number == 0: 
    print("Numero é Neutro")
elif (number%2) == 0:
    print("Numero é Par")
else: 
    print("Numero é Impar")