nome = str(input("Digite seu nome completo: "))
nomeDividido = nome.split()
nomeSemEspaco = nome.replace(" ", "")
upper = nome.upper()
lower = nome.lower()

print(f"Seu nome em maiúsculas é {upper}.")
print(f"Seu nome em minúsculas é {lower}.")
print(f"Seu nome tem um total de {len(nomeSemEspaco)} letras.")
print(f"Seu primeiro nome é {nomeDividido[0]} e tem {len(nomeDividido[0])} letras.")