meuSalario = float(input("Digite seu salário e eu lhe darei um aumento: "))

salMinimo = 1250.00
aumento10 = meuSalario * 10 / 100
aumento15 = meuSalario * 15 / 100

if meuSalario <= salMinimo:
    meuSalario + aumento15
    print(f"Seu salário de R${meuSalario} receberá um aumento de 15%, um adicional de R${aumento15:.2f}\n Seu novo salário é de {meuSalario + aumento15:.2f}")
else:
    meuSalario + aumento10
    print(f"Seu salário de R${meuSalario} receberá um aumento de 10%, um adicional de R${aumento10:.2f}\n Seu novo salário é de {meuSalario + aumento10:.2f}")