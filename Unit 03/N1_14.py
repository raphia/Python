#Analisador de Triângulos: Peça o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# de inicio é só lado qualquer depois das condições sera maior
lado_maior =  float(input("Digite o primeiro lado do Triangulo: "))
cat_a = float(input("Digite o segundo lado do Trinangulo: "))
cat_b = float(input("Digite o terceiro lado do Trinangulo: "))



if lado_maior < cat_a: 
    #Cache guarda valor do lado maior para não se perder na troca
    cache = lado_maior
    lado_maior = cat_a
    cat_a = cache

if (lado_maior < cat_b):
    #Cache guarda valor do lado maior para não se perder na troca
    cache = lado_maior
    lado_maior = cat_b
    cat_b = cache


if lado_maior < (cat_a+cat_b): 
    print("FORMA TRIANGULO")
else:
    print("Não forma Triangulo")
    