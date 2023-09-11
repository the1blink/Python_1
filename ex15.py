kmRodados = float(input("Digite a quantidade de KMs rodados: "))
diasAlugados = int(input("Por quantos dias o carro foi alugado: "))

preco = diasAlugados * 60 + kmRodados * 0.15

print(f"Após rodar {kmRodados}KMs por {diasAlugados} dias, o valor a ser pago é: R${preco:.2f}")