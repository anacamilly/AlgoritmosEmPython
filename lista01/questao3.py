vi = float(input("Digite o valor inicial da aplicação: R$"))

n = int(input("Digite o número de meses da aplicação: "))

i = float(input("Digite a taxa de juros da aplicação: "))

vf = ((1 + i) ** n) * vi
print("O valor final da aplicação será: R$" + str(round(vf, 2)))