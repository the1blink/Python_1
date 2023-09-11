nome = str(input("Digite seu nome completo: ")).strip()

nomeDividido = nome.split()
ultimoNome = nomeDividido[-1]

print(f"Seu primeiro nome é {nomeDividido[0]}, e o último é {ultimoNome}.")