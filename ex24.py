cidade = str.strip(input("Digite o nome da sua cidade: ")).title()

cidadeSplitada = cidade.split()

checaSanto = ("Santo" in cidadeSplitada[0])
checaSão = ("São" in cidadeSplitada[0])

if checaSanto is True:
    print(f"{cidade} começa com 'Santo'.")
elif checaSão is True:
    print(f"{cidade} começa com 'São'.")
else:
    print(f"{cidade} não começa com 'Santo' ou 'São'.")