""" nome =  str(input("Escreva seu nome: ")).capitalize()

if nome == "Matheus":
    print(f"Belo nome, {nome}.")
else:
    print("Não gostei do seu nome.")
print("Tenha um bom dia") """

n1 = float(input("Digite a primera nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print(f"Aluno aprovado com média {media:.1f}")
else:
    print(f"Aluno reprovado com média {media:.1f}")