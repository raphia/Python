#N1_03 Conversor de Medidas: Peça um valor em metros e exiba convertido em centímetros e milímetros.

measure = float(input("Digite a Medida em Metros: "))

##  a questão pede algo do tipo : 
## centrimetro = measure * 100
## milimetro = measure * 1000
## Assim seria sem graça que tal matar todas metidas em GERAL!!!! 

## OBSERVE A ESCALA!!!
## km - hm - dam - [ m ] - dm - cm - mm
## na cara se metro unidade dm vem de 100 , dm vem de 10 cm vem de 100 , mm vem de mil aqui se multiplica
## parte oposta se divida pq maior que metro dam 10 , hm 100 e km 1000 nesse caso se divide!!! 


m = measure
dm = m * 10
cm = dm * 10
mm = cm * 10
dam = m / 10
hm = dam / 10
km = hm / 10


print(f"Centímetros : {cm:.2f} & Milímetros : {mm:.2f}")
print("Modifica o codigo e tenta brincar outros valores! ")