#N1_11 Alistamento Militar: Peça o ano de nascimento. Se ele tiver menos de 18 anos, 
# diga quanto tempo falta para o alistamento. Se tiver 18, diga que é a hora. Se tiver mais, diga quanto tempo passou do prazo.
import datetime

born_year = int(input("Digite o ano de nascimento: "))
year_of_today = datetime.datetime.now().year
temp = year_of_today-born_year

if(born_year < 0):
    print("Engraçadinho quer botar numero negativo, não calculo nada Antes de Cristo [AC]! ")
else:
    if(temp == 0):
        print("Individuo acabou de nascer? então!!!")
    if(temp > 125):
        print(f"Multate ou Undead? Com {temp} anos ainda está vivo? então!!! ")
    if born_year > year_of_today: 
        print("Você veio do futuro, ou data desse computador está errada? ")
    elif temp > 18:
        print(f"Você passou do prazo, tempo de atrazo {temp-18} ano(s)")
    elif temp == 18:
        print("Está na hora de se alistar")
    else: 
        print(f"Falta {18-temp} ano(s) para o alistamento")
