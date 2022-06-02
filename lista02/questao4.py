altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: (F ou M) ")

if sexo == "F":
    peso = ((72.7 * altura) - 58)
    print("Seu peso ideal é: " + str(peso))
else:
    peso = ((62.1 * altura) - 44.7)
    print("Seu peso ideal é: " + str(peso))