import math

angulo = int(input("Digite um radianos de qualquer valor: "))

radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"O seno, cosseno e tangente de {angulo} valem respectivamente: {seno:.2f}, {cosseno:.2f} e {tangente:.2f}")