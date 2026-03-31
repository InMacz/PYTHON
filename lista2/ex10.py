turno = input("Em que turno você estuda?, M - Matutino, V - Verspertino ou N - Noturno : ")
if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")