votosBrancos = int(input("Digite a quantidade de votos brancos: "))

votosNulos = int(input("Digite a quantidade de votos nulos: "))

votosValidos = int(input("Digite a quantidade de votos válidos: "))

totalVotos = votosBrancos + votosNulos + votosValidos
percentualVotosBrancos = 100*(votosBrancos/totalVotos)
percentualVotosNulos = 100*(votosNulos/totalVotos)
percentualVotosValidos = 100*(votosValidos/totalVotos)
print("O percentual de votos brancos foi: " + str(percentualVotosBrancos) + "%")
print("O percentual de votos nulos foi: " + str(percentualVotosNulos) + "%")
print("O percentual de votos válidos foi: " + str(percentualVotosValidos) + "%")