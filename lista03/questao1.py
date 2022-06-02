for i in range(10):
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    media = (nota1 + nota2 + nota3) / 3
    print("Média do aluno " + str(i + 1) + ": " + str(media))

# Atividade 1 - A
    maior = 0
    menor = 10
    for i in range(2):
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        media = (nota1 + nota2 + nota3) / 3
        print("Média do aluno " + str(i + 1) + ": " + str(round(media, 2)))
        if (media > maior):
            maior = media
        if (media < menor):
            menor = media
    print("Maior média: " + str(round(maior, 2)))
    print("Menor média: " + str(round(menor, 2)))

# Atividade 1 - B
    numero_alunos = 3
    maior = 0
    menor = 10
    aprovados = 0
    for i in range(numero_alunos):
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        media = (nota1 + nota2 + nota3) / 3
        print("Média do aluno " + str(i + 1) + ": " + str(round(media, 2)))
        if (media > maior):
            maior = media
        if (media < menor):
            menor = media
        if (media >= 7):
            aprovados += 1

    print("Maior média: " + str(round(maior, 2)))
    print("Menor média: " + str(round(menor, 2)))
    percentual = round((aprovados / numero_alunos) * 100, 2)
    print("Percentual de alunos aprovados: " + str(percentual) + "%")
