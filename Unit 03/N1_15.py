#N1_15 Gerenciador de Pagamentos: Calcule o valor a ser pago por um produto, 
# considerando o preço normal e a condição de pagamento:
#
#    À vista dinheiro/cheque: 10% de desconto.
#
#    À vista no cartão: 5% de desconto.
#
#    Em até 2x no cartão: preço formal.
#
#    3x ou mais no cartão: 20% de juros.

price = float(input("Digite o valor do Produto R$: "))
print("#"*20)
print("Forma pagamento")
print(f"1 : À vista dinheiro/cheque: 10% de desconto.")
print(f"2: À vista no cartão [DEBITO]: 5% de desconto.")
print(f"3: Em até 2x no cartão: Sem Juros")
print(f"4: 3x ou mais no cartão: 20% de juros.")
print("#"*20)
opt = int(input("OPÇÃO: "))

##Existe o CASE que é muito melhor para esse caso no entando
## aqui por enquanto é para usar if elif e else
## mas sim essa questão merecia um loop tipo while para ficar simulando maquina de caixa
## depois entrar no CASE para opções! e retornar a resposta correta!

if (opt == 1):
    price = price - (price*0.10)
    print("FORMA: À vista")
    print(f"VALOR: R$ {price:.2f}")
elif (opt == 2):
    price = price - (price*0.05)
    print("FORMA: Debito Cartão")
    print(f"VALOR: R$ {price:.2f}")
elif (opt == 3):
    print("FORMA: Divido 2x")
    print(f"VALOR: R$ {price:.2f} em parcelas 2x de {(price/2):.2f}")
elif (opt == 4):
    #Observe que essa é a forma só para acabar questão de IF , ELIF e ELSE e para essa questão ficar
    #perfeira era preciso usar laços e loops
    print("FORMA: Divido 3x ou mais")
    print(f"VALOR FINAL R$ {(price*1.20):.2f} ")
else: 
    print("Opção Digitada está incorreta!")