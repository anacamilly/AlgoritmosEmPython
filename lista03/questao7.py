contador = 0
while (True):
    numero = int(input("Entre com um número... "))
    if (numero == 0):
        break
    if (numero >= 100 and numero <= 200):
        contador += 1

print("Foram digitados " + str(contador) + " números entre 100 e 200")
