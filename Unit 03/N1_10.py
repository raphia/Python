#N1_10 Custo da Viagem: Pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#  cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

distance = int(input("Digite a quilometragem da viagem em km: "))

if distance <= 200: 
    value = 0.5 * distance
    print(f"Valor da viagem será de : R$ {value:.2f}")
else: 
    value = 0.45 * distance
    print(f"Valor da viagem será de : R$ {value:.2f}")