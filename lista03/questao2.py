a1 = int(input("Entre com o valor inicial: "))
n = int(input("Entre com o número de elementos da PA: "))
r = int(input("Entre com a razão da PA: "))
print(a1, end=" ")
for i in range(n-1):
    a1 = a1 + r
    print(a1, end=" ")

a1 = int(input("Entre com o valor inicial: "))
n = int(input("Entre com o número de elementos da PA: "))
r = int(input("Entre com a razão da PA: "))

for i in range(a1, (a1 + (n-1)*r) + 1, r):
    print(i, end=" ")