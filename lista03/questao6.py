h_chico = 150
h_juca = 110
anos = 0

while (h_chico >= h_juca):
    h_chico += 2
    h_juca += 3
    anos += 1

print("Passaram-se " + str(anos) + " anos...")
print("Juca está com " + str(h_juca/100) + "m")
print("Chico está com " + str(h_chico/100) + "m")