#Média Escolar 2.0: Calcule a média de duas notas. Abaixo de 5.0: REPROVADO. 
# Entre 5.0 e 6.9: RECUPERAÇÃO. 7.0 ou superior: APROVADO.

grade_one = float(input("Digite a primeira nota: "))
grade_two = float(input("Digite a segunda nota: "))

average = (grade_one+grade_two)/2

if average < 5:
    print(f"REPROVADO: [MEDIA = {average:.1f} ]")
elif average >= 7:
    print(f"APROVADO: [MEDIA = {average:.1f} ]")
else: 
    print(f"RECUPERAÇÃO: [MEDIA = {average:.1f} ]")