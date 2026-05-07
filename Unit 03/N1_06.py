##Radar Eletrônico: Peça a velocidade de um carro. Se ultrapassar 80km/h, 
# exiba uma mensagem dizendo que ele foi multado. A multa custa R$ 7,00 por cada km acima do limite.

speed_car = int(input("Digite a velocidade do carro em KM/H: "))

if speed_car > 80:
    car_fine = (speed_car - 80)*7
    print(f"Velocidade acima do Padrão: {speed_car} Km/h")
    print(f"Velocidade adicional de:  {(speed_car - 80)} Km/h")
    print(f"Multa de R$ {car_fine:.2f}")
else:
    print(f"Velocidade permitida: {speed_car} Km/h")
    print(f"Boa viagem! Diriga com Segurança!")