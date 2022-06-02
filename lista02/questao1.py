salario = float(input("Digite o valor do salário: R$"))

if salario < 1500:
    aumento = salario * 0.25
    novoSalario = salario + aumento
elif salario >= 1500 and salario < 3200:
    aumento = salario * 0.10
    novoSalario = salario + aumento
elif salario >= 3200:
    aumento = salario * 0.05
    novoSalario = salario + aumento

print("Salario atualizado: " + str(round(novoSalario, 2)))
