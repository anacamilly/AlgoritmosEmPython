while (True):
    numero = int(input("Digite o número que você deseja testar... "))
    if (numero == 0):
        break
    i = 1
    multiplicacao = i * (i+1) * (i+2)

    while (multiplicacao < numero):
        i += 1
        multiplicacao = i * (i + 1) * (i + 2)

        if (multiplicacao == numero):
            print("O número " + str(numero) + " é triangular (" + str(i)
                  + "," + str(i + 1) + "," + str(i + 2) + ")!")
        else:
            print("O número " + str(numero) + " não é triangular!")

        print("Fim :)")