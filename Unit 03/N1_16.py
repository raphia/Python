#O seu programa precisa fazer o seguinte:
#
#   Fazer uma pergunta na tela: "Qual a temperatura atual da sua CPU?"
#
#    Esperar o usuário digitar o número da temperatura.
#
#    Analisar esse número usando as seguintes regras:
#
#        Se o número for maior que 75: Exiba a mensagem "Alerta! O processador está muito quente."
#
#        Se o número for entre 50 e 75: Exiba a mensagem "Temperatura moderada."
#
#        Se o número for menor que 50: Exiba a mensagem "Temperatura segura."

temp = int(input("Qual a temperatura da sua CPU: "))
if (temp > 75):
    print("Alerta!!!! O Processador está muito quente.")
elif (temp < 50):
    print("Temperatura Segura!")
else:
    print("Temperatura moderada")