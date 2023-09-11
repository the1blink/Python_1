preco = float(input("Escreva o valor do produto: R$"))
porcentoOff = int(input("Escreva quantos % tem de desconto: %"))

desconto = preco * porcentoOff / 100
precoFinal = preco - desconto

print(f"Com {porcentoOff}% de desconto, você pagará R${desconto} a menos, e o novo preço é R${precoFinal:.2f}")