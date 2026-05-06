#Calculadora de Desconto: Peça o preço de um produto e aplique 10% de desconto. Exiba o novo preço na tela.

print("### DESCONTO 10% ####")
valor = float(input("Digite o preço do produto: R$ "))
desconto = 0.10
pay_valor = valor - (valor*desconto)
# Outra maneira bem simples de fazer mas não intuitiva
# pay_valor = valor * 0.90
# Se existe um desconto de 10% é porque vai pagar 90%! 

print(f"Valor a pagar é de R$ {pay_valor:0.2f}")