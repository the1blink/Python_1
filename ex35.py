a = int(input("Verificarei se um triângulo é possível. Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and b + c > a and a + c > b and a - b < c and b - c < a and a - c < b:
    print(f"Um triângulo formado por {a}, {b} e {c} é matemáticamente possível.")
else:
    print(f"Um triângulo formado por {a, b} e {c} é matemáticamente impossível.")