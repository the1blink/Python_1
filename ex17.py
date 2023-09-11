import math

catOposto = int(input("Digite o comprimento do cateto oposto: "))
catAdjacente = int(input("Digite o comprimento do catato adjacente: "))

""" hipotenusa = sqrt(catOposto ** 2 + catAdjacente ** 2)"""
hipotenusa = math.hypot(catOposto, catAdjacente)


print(f"O comprimento da hipotenusa do triangulo descrito é {hipotenusa:.3f}")