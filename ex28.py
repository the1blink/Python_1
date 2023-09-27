import random

numCPU = random.randint(0, 5)

guess = int(input("Pensei em um número de 0 a 5. Tente adivinhar qual: "))

if guess == numCPU:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, você errou! O número era {numCPU}")