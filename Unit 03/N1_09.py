##Aumento Salarial: Se o salário for superior a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

wage = float(input("Digite o Salario R$: "))

#DICA DE MESTRE!!! Aumento de 10% mesmo que ter salario de 110% em relação ao que era
#Mesma logica 15% é mesmo de 115% de aumento ou seja uso 1.10 e 1.15 é extremamente simples

if wage > 1250: 
    print(f"Aumento do salario será de 10% ou seja novo Salario = R$ {(wage*1.10):.2f}")
else:
    print(f"Aumento do salario será de 15% ou seja novo Salario = R$ {(wage*1.15):.2f}")