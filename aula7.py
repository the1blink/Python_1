n1 = float(input("Escreva um número: "))
n2 = float(input("Escreva mais um número: "))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
divi = n1 / n2
potencia = n1 ** n2
diviInt = n1 // n2
diviResto = n1 % n2

print (f"A soma desses números é igual a {soma}")
print (f"O primeiro número subtraído pelo segundo é igual a {sub}")
print (f"A multiplicação entre esses números é igual a {multi}")
print (f"O primeiro número dividido pelo segundo é igual a {divi:.3f}")
print (f"O primeiro número elevado ao segundo é igual a {potencia}")
print (f"A divisão inteira do primeiro número pelo segundo é igual a {diviInt}")
print (f"O resto da divisão entre o primeiro número e o segundo é igual a {diviResto}")


""" É possível calcular a raíz quadrada de um número ao eleva-lo à meio (1/2). Pode-se utilizar o comando pow() ou fazer com o operador mesmo.
Também é possível calcular a raíz cúbica, elevando ao seu terço (1/3). A sintaxe é a mesma."""

""" Para limitar o número de caractéres em uma resposta, é posível formatar utilizando ":.3f", ou qualquer número no lugar do 3, para que ele
limite a quantidade ou acrescente [ver linha 15 para exemplo] """

""" Para quebrar linha, utiliza-se o \n, e isso serve para não ter a necessidade de escrever um monte de print. Para não quebrar a linha, usa-se ", end = "  "
"""