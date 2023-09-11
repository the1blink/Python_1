nome = str.title(input("Digite seu nome completo: ")).strip()

checaSilva = ("Silva" in nome)

if (checaSilva is True):
    print(f"Seu sobrenome tem Silva.") 
else:
    print("Silva não é um dos seus sobrenomes.")