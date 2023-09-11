frase = str.lower(input("Digite uma frase qualquer: ")).strip()
primeiraInstancia = frase.find("a") 
ultimaInstancia = frase.rfind("a")

print(f"A letra 'a' aparece {frase.count('a')} vezes na frase '{frase.capitalize()}'.")
print(f"A primeira vez que 'a' aparece nessa frase é na posição {primeiraInstancia}, e a última, na posição {ultimaInstancia}.")