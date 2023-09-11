salario = float(input("Digite seu salário atual: R$"))
qntAumentou = float(input("Digite quantos % de aumento você recebeu: "))

aumento = salario * qntAumentou / 100

novoSalario = salario + aumento

print(f"Você recebeu um aumento de {qntAumentou}%, e seu novo salário é {novoSalario:.2f}R$, um adicional de {aumento:.2f}R$")