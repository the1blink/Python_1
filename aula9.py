frase = "Curso em video Python"
fraseComEspaco = "      Curso em video Python       "


print(frase[:8])

print(frase[9:])

print(frase[2:21:2])

print(len(frase))

print(frase.count("o"))

print(frase.count("o", 0, 13))

print(frase.find("deo"), frase.find("Android"))

print("CURSO" in frase)

print(frase.replace("Python", "Android"))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

print(fraseComEspaco)
print(fraseComEspaco.strip()) #esse aqui dá pra cortar os espaços do lado direito ou esquerdo com Rstrip

print("-".join(frase))
print(frase.split())