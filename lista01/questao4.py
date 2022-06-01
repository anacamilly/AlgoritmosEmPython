import math
print("Indique as coordenadas x e y do ponto 1:")
x1 = float(input())
y1 = float(input())

print("Indique as coordenadas x e y do ponto 2:")
x2 = float(input())
y2 = float(input())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)

print("A distância entre os dois pontos é: " + str(distancia))