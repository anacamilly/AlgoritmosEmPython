distanciaPercorrida = float(input("Digite a distância percorrida (km): "))
volumeCombustivelGasto = float(input("Digite o volume de combustível que foi gasto (l):"))
precoDoCombustivel = float(input("Digite o preço do combustível (R$/l): "))

precoKmRodado = precoDoCombustivel * (1/distanciaPercorrida) * volumeCombustivelGasto
# precoKmRodado = volumeCombustivelGasto/distanciaPercorrida * precoDoCombustivel
print("O preço do km rodado é: R$" + str(round(precoKmRodado, 2)))
