##Calculadora de Área: Peça a largura e a altura de uma parede em metros. 
# Calcule a área e a quantidade de tinta necessária para pintá-la (considerando que cada litro de tinta pinta 2m²).

width = float(input("Digite a largura em metros: "))
height = float(input("Digite a altura em metros: "))

area = width * height

## Se cada litro de tinta pinta 2 metros quadrados! ou seja Area / 2 !!!

ink = area / 2

print(f"Vai ser preciso de {ink:.1f} litros de tinta")