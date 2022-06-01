cabecas = int(input("Indique a quantidade de cabeças: "))
patas = int(input("Indique a quantidade de patas: "))

coelhos = int((patas - 2*cabecas)/2)
patos = int(cabecas - coelhos)

print("Coelhos: " + str(coelhos))
print("Patos: " + str(patos))