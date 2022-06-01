print("Informe a sua idade em anos, meses e dias, respectivamente:")
anos = int(input())
meses = int(input())
dias = int(input())

idadeEmDias = (anos*365)+(meses*30)+dias

print("A minha idade aproximada em dias é de: " + str(idadeEmDias))
