n = int(input("Entre com um número: "))
for i in range(n-1, 0, -1):
    n = n * i
print("O valor do fatorial é: " + str(n))