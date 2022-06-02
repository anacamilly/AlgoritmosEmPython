a = int(input("Digite  um valor para A: "))
b = int(input("Digite  um valor para B: "))
i = int(input("Digite um valor para i: (1,2,3)"))

if i == 1:
    resultado = a + b
    print("O resultado é: " + str(resultado))
elif i == 2:
    resultado = a - b
    print("O resultado é: " + str(resultado))
elif i == 3:
    resultado = a * b
    print("O resultado é: " + str(resultado))