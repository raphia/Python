#Média de Notas: Peça 3 notas ao usuário e exiba a média aritmética.

grade_one = float(input("Digite a primeira nota: "))
grade_two = float(input("Digite a segunda nota: "))
grade_tree = float(input("Digite a terceira nota: "))

media = (grade_one+grade_two+grade_tree)/3

print(f"Media foi: {media:.1f}")