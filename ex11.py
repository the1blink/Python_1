largura = float(input("Escreva a largura da parede em metros: "))
altura = float(input("Escreva a altura da parede em metros: "))

area = largura * altura
tinta = area / 2

print(f"A área da sua parede é de {area}m², cada litro de tinta pinta 2m², logo você precisará de {tinta}L de tinta para pintar toda a parede. ")