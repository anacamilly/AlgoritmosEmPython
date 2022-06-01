apostaAmigo1 = float(input("Digite o valor da aposta do amigo 1: R$"))
apostaAmigo2 = float(input("Digite o valor da aposta do amigo 2: R$"))

totalAposta = apostaAmigo1 + apostaAmigo2
pAmigo1 = apostaAmigo1/totalAposta
pAmigo2 = apostaAmigo2/totalAposta

premio = float(input("Qual o valor do prêmio: R$"))
premioAmigo1 = premio * pAmigo1
premioAmigo2 = premio * pAmigo2

print("O prêmio do amigo 1 é R$" + str(round(premioAmigo1, 2)))
print("O prêmio do amigo 2 é R$" + str(round(premioAmigo2, 2)))
