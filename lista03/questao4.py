n = int(input("Entre com um número: "))

fib0 = 0
fib1 = 1

print(fib0, end=" ")
print(fib1, end=" ")

for i in range(n-2):
    proximo_elemento = fib0 + fib1
    fib0 = fib1
    fib1 = proximo_elemento
    print(proximo_elemento, end=" ")
