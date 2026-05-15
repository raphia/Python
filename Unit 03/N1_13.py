#Classificando Atletas: A Confederação Nacional de Natação precisa de um programa que leia 
#  ano de nascimento de um atleta e mostre sua categoria:
#    Até 9 anos: MIRIM
#    Até 14 anos: INFANTIL
#    Até 19 anos: JUNIOR
#    Até 25 anos: SÊNIOR
#    Acima de 25: MASTER
import datetime

born_year = int(input("Digite o ano de Nascimento do Atleta: "))
recent_year = datetime.datetime.now().year
old_player = recent_year-born_year

if old_player > 25:
    print(f"MASTER idade: [{old_player}]")
elif old_player > 19: 
    print(f"SÊNIOR idade: [{old_player}]")
elif old_player > 14:
    print(f"JUNIOR idade: [{old_player}]")
elif old_player > 9:
    print(f"INFANTIL idade: [{old_player}]")
else: 
    print(f"MIRIM idade: [{old_player}]")