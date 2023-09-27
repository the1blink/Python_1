velLimite = 80.0
velCar = float(input(f"A velocidade máxima da estrada é {velLimite}Km/h. Para cada Km/h acima do limite, você será multado em R$7,00. Digite a velocidade do carro: "))
multa = 7.0 * (velCar - velLimite)

if velCar > velLimite:
    print(f"Seu carro estava a {velCar}Km/h. Você será multado em R${multa}")
elif velCar == velLimite:
    print(f"Você está a {velCar}Km/h e no limite de velocidade, diminua!")
elif velCar >= velLimite - 7:
    print(f"Você está a {velCar}Km/h e quase ultrapassando o limite, diminua!")
else:
    print("Boa viagem!")
