capDePreço = 200

distancia = float(input(f"Nesta empresa, cobramos R$0,50 por Km para viagens de até {capDePreço}Km, e R$0,45 por Km para viagens maiores. Digite quantos Km de distancia até o destino: "))

valor1 = 0.50
valor2 = 0.45
valorFinal = None

if distancia <= capDePreço:
    valorFinal = distancia * valor1
    print(f"Sua viagem de {distancia}Km custará R${valorFinal:.2f}")
elif distancia > capDePreço:
    valorFinal = distancia * valor2
    print(f"Sua viagem de {distancia}Km custará R${valorFinal:.2f}")